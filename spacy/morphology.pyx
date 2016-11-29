from os import path
from .lemmatizer import Lemmatizer

try:
    import ujson as json
except ImportError:
    import json

from .parts_of_speech import IDS as POS_IDS
from .parts_of_speech cimport ADJ, VERB, NOUN, PUNCT
from .attrs cimport IS_SPACE
from .lexeme cimport Lexeme


cdef class Morphology:
    def __init__(self, StringStore string_store, tag_map, lemmatizer):
        self.mem = Pool()
        self.strings = string_store
        self.tag_map = tag_map
        self.lemmatizer = lemmatizer
        self.n_tags = len(tag_map) + 1
        self.tag_names = tuple(sorted(tag_map.keys()))
        self.reverse_index = {}
        
        self.rich_tags = <RichTagC*>self.mem.alloc(self.n_tags, sizeof(RichTagC))
        for i, (tag_str, props) in enumerate(sorted(tag_map.items())):
            self.rich_tags[i].id = i
            self.rich_tags[i].name = self.strings[tag_str]
            self.rich_tags[i].morph = 0
            self.rich_tags[i].pos = POS_IDS[props['pos'].upper()]
            self.reverse_index[self.rich_tags[i].name] = i
        self._cache = PreshMapArray(self.n_tags)

    def __reduce__(self):
        return (Morphology, (self.strings, self.tag_map, self.lemmatizer), None, None)

    cdef int assign_tag(self, TokenC* token, tag) except -1:
        if isinstance(tag, basestring):
            tag_id = self.reverse_index[self.strings[tag]]
        else:
            tag_id = self.reverse_index[tag]
        self.assign_tag_id(token, tag_id)

    cdef int assign_tag_id(self, TokenC* token, int tag_id) except -1:
        if tag_id >= self.n_tags:
            raise ValueError("Unknown tag ID: %s" % tag_id)
        # TODO: It's pretty arbitrary to put this logic here. I guess the justification
        # is that this is where the specific word and the tag interact. Still,
        # we should have a better way to enforce this rule, or figure out why
        # the statistical model fails.
        # Related to Issue #220
        if Lexeme.c_check_flag(token.lex, IS_SPACE):
            tag_id = self.reverse_index[self.strings['SP']]
        analysis = <MorphAnalysisC*>self._cache.get(tag_id, token.lex.orth)
        if analysis is NULL:
            analysis = <MorphAnalysisC*>self.mem.alloc(1, sizeof(MorphAnalysisC))
            analysis.tag = self.rich_tags[tag_id]
            tag_str = self.strings[self.rich_tags[tag_id].name]
            analysis.lemma = self.lemmatize(analysis.tag.pos, token.lex.orth,
                                            **self.tag_map.get(tag_str, {}))
            self._cache.set(tag_id, token.lex.orth, analysis)
        token.lemma = analysis.lemma
        token.pos = analysis.tag.pos
        token.tag = analysis.tag.name
        token.morph = analysis.tag.morph

    cdef int assign_feature(self, uint64_t* morph, feature, value) except -1:
        pass

    def load_morph_exceptions(self, dict exc):
        # Map (form, pos) to (lemma, rich tag)
        cdef unicode pos_str
        cdef unicode form_str
        cdef unicode lemma_str
        cdef dict entries
        cdef dict props
        cdef int lemma
        cdef attr_t orth
        cdef attr_t tag_id
        cdef int pos
        cdef RichTagC rich_tag
        for tag_str, entries in exc.items():
            tag = self.strings[tag_str]
            tag_id = self.reverse_index[tag] 
            rich_tag = self.rich_tags[tag_id]
            for form_str, props in entries.items():
                cached = <MorphAnalysisC*>self.mem.alloc(1, sizeof(MorphAnalysisC))
                cached.tag = rich_tag
                orth = self.strings[form_str]
                for name_str, value_str in props.items():
                    if name_str == 'L':
                        cached.lemma = self.strings[value_str]
                    else:
                        self.assign_feature(&cached.tag.morph, name_str, value_str)
                if cached.lemma == 0:
                    cached.lemma = self.lemmatize(rich_tag.pos, orth,
                                                  self.tag_map.get(tag_str, {}))
                self._cache.set(tag_id, orth, <void*>cached)

    def lemmatize(self, const univ_pos_t univ_pos, attr_t orth, **morphology):
        cdef unicode py_string = self.strings[orth]
        if self.lemmatizer is None:
            return self.strings[py_string.lower()]
        if univ_pos not in (NOUN, VERB, ADJ, PUNCT):
            return self.strings[py_string.lower()]
        cdef set lemma_strings
        cdef unicode lemma_string
        lemma_strings = self.lemmatizer(py_string, univ_pos, **morphology)
        lemma_string = sorted(lemma_strings)[0]
        lemma = self.strings[lemma_string]
        return lemma

IDS = {
    "Animacy_anim": Animacy_anim,
    "Animacy_inam": Animacy_inam,
    "Aspect_freq": Aspect_freq,
    "Aspect_imp": Aspect_imp,
    "Aspect_mod": Aspect_mod,
    "Aspect_none": Aspect_none,
    "Aspect_perf": Aspect_perf,
    "Case_abe": Case_abe,
    "Case_abl": Case_abl,
    "Case_abs": Case_abs,
    "Case_acc": Case_acc,
    "Case_ade": Case_ade,
    "Case_all": Case_all,
    "Case_cau": Case_cau,
    "Case_com": Case_com,
    "Case_dat": Case_dat,
    "Case_del": Case_del,
    "Case_dis": Case_dis,
    "Case_ela": Case_ela,
    "Case_ess": Case_ess,
    "Case_gen": Case_gen,
    "Case_ill": Case_ill,
    "Case_ine": Case_ine,
    "Case_ins": Case_ins,
    "Case_loc": Case_loc,
    "Case_lat": Case_lat,
    "Case_nom": Case_nom,
    "Case_par": Case_par,
    "Case_sub": Case_sub,
    "Case_sup": Case_sup,
    "Case_tem": Case_tem,
    "Case_ter": Case_ter,
    "Case_tra": Case_tra,
    "Case_voc": Case_voc,
    "Definite_two": Definite_two,
    "Definite_def": Definite_def,
    "Definite_red": Definite_red,
    "Definite_ind": Definite_ind,
    "Degree_cmp": Degree_cmp,
    "Degree_comp": Degree_comp,
    "Degree_none": Degree_none,
    "Degree_pos": Degree_pos,
    "Degree_sup": Degree_sup,
    "Degree_abs": Degree_abs,
    "Degree_com": Degree_com,
    "Degree_dim ": Degree_dim, # du
    "Gender_com": Gender_com,
    "Gender_fem": Gender_fem,
    "Gender_masc": Gender_masc,
    "Gender_neut": Gender_neut,
    "Mood_cnd": Mood_cnd,
    "Mood_imp": Mood_imp,
    "Mood_ind": Mood_ind,
    "Mood_n": Mood_n,
    "Mood_pot": Mood_pot,
    "Mood_sub": Mood_sub,
    "Mood_opt": Mood_opt,
    "Negative_neg": Negative_neg,
    "Negative_pos": Negative_pos,
    "Negative_yes": Negative_yes,
    "Number_com": Number_com,
    "Number_dual": Number_dual,
    "Number_none": Number_none,
    "Number_plur": Number_plur,
    "Number_sing": Number_sing,
    "Number_ptan ": Number_ptan, # bg
    "Number_count ": Number_count, # bg
    "NumType_card": NumType_card,
    "NumType_dist": NumType_dist,
    "NumType_frac": NumType_frac,
    "NumType_gen": NumType_gen,
    "NumType_mult": NumType_mult,
    "NumType_none": NumType_none,
    "NumType_ord": NumType_ord,
    "NumType_sets": NumType_sets,
    "Person_one": Person_one,
    "Person_two": Person_two,
    "Person_three": Person_three,
    "Person_none": Person_none,
    "Poss_yes": Poss_yes,
    "PronType_advPart": PronType_advPart,
    "PronType_art": PronType_art,
    "PronType_default": PronType_default,
    "PronType_dem": PronType_dem,
    "PronType_ind": PronType_ind,
    "PronType_int": PronType_int,
    "PronType_neg": PronType_neg,
    "PronType_prs": PronType_prs,
    "PronType_rcp": PronType_rcp,
    "PronType_rel": PronType_rel,
    "PronType_tot": PronType_tot,
    "PronType_clit": PronType_clit,
    "PronType_exc ": PronType_exc, # es, ca, it, fa,
    "Reflex_yes": Reflex_yes,
    "Tense_fut": Tense_fut,
    "Tense_imp": Tense_imp,
    "Tense_past": Tense_past,
    "Tense_pres": Tense_pres,
    "VerbForm_fin": VerbForm_fin,
    "VerbForm_ger": VerbForm_ger,
    "VerbForm_inf": VerbForm_inf,
    "VerbForm_none": VerbForm_none,
    "VerbForm_part": VerbForm_part,
    "VerbForm_partFut": VerbForm_partFut,
    "VerbForm_partPast": VerbForm_partPast,
    "VerbForm_partPres": VerbForm_partPres,
    "VerbForm_sup": VerbForm_sup,
    "VerbForm_trans": VerbForm_trans,
    "VerbForm_gdv ": VerbForm_gdv, # la,
    "Voice_act": Voice_act,
    "Voice_cau": Voice_cau,
    "Voice_pass": Voice_pass,
    "Voice_mid ": Voice_mid, # gkc,
    "Voice_int ": Voice_int, # hb,
    "Abbr_yes ": Abbr_yes, # cz, fi, sl, U,
    "AdpType_prep ": AdpType_prep, # cz, U,
    "AdpType_post ": AdpType_post, # U,
    "AdpType_voc ": AdpType_voc, # cz,
    "AdpType_comprep ": AdpType_comprep, # cz,
    "AdpType_circ ": AdpType_circ, # U,
    "AdvType_man": AdvType_man,
    "AdvType_loc": AdvType_loc,
    "AdvType_tim": AdvType_tim,
    "AdvType_deg": AdvType_deg,
    "AdvType_cau": AdvType_cau,
    "AdvType_mod": AdvType_mod,
    "AdvType_sta": AdvType_sta,
    "AdvType_ex": AdvType_ex,
    "AdvType_adadj": AdvType_adadj,
    "ConjType_oper ": ConjType_oper, # cz, U,
    "ConjType_comp ": ConjType_comp, # cz, U,
    "Connegative_yes ": Connegative_yes, # fi,
    "Derivation_minen ": Derivation_minen, # fi,
    "Derivation_sti ": Derivation_sti, # fi,
    "Derivation_inen ": Derivation_inen, # fi,
    "Derivation_lainen ": Derivation_lainen, # fi,
    "Derivation_ja ": Derivation_ja, # fi,
    "Derivation_ton ": Derivation_ton, # fi,
    "Derivation_vs ": Derivation_vs, # fi,
    "Derivation_ttain ": Derivation_ttain, # fi,
    "Derivation_ttaa ": Derivation_ttaa, # fi,
    "Echo_rdp ": Echo_rdp, # U,
    "Echo_ech ": Echo_ech, # U,
    "Foreign_foreign ": Foreign_foreign, # cz, fi, U,
    "Foreign_fscript ": Foreign_fscript, # cz, fi, U,
    "Foreign_tscript ": Foreign_tscript, # cz, U,
    "Foreign_yes ": Foreign_yes, # sl,
    "Gender_dat_masc ": Gender_dat_masc, # bq, U,
    "Gender_dat_fem ": Gender_dat_fem, # bq, U,
    "Gender_erg_masc ": Gender_erg_masc, # bq,
    "Gender_erg_fem ": Gender_erg_fem, # bq,
    "Gender_psor_masc ": Gender_psor_masc, # cz, sl, U,
    "Gender_psor_fem ": Gender_psor_fem, # cz, sl, U,
    "Gender_psor_neut ": Gender_psor_neut, # sl,
    "Hyph_yes ": Hyph_yes, # cz, U,
    "InfForm_one ": InfForm_one, # fi,
    "InfForm_two ": InfForm_two, # fi,
    "InfForm_three ": InfForm_three, # fi,
    "NameType_geo ": NameType_geo, # U, cz,
    "NameType_prs ": NameType_prs, # U, cz,
    "NameType_giv ": NameType_giv, # U, cz,
    "NameType_sur ": NameType_sur, # U, cz,
    "NameType_nat ": NameType_nat, # U, cz,
    "NameType_com ": NameType_com, # U, cz,
    "NameType_pro ": NameType_pro, # U, cz,
    "NameType_oth ": NameType_oth, # U, cz,
    "NounType_com ": NounType_com, # U,
    "NounType_prop ": NounType_prop, # U,
    "NounType_class ": NounType_class, # U,
    "Number_abs_sing ": Number_abs_sing, # bq, U,
    "Number_abs_plur ": Number_abs_plur, # bq, U,
    "Number_dat_sing ": Number_dat_sing, # bq, U,
    "Number_dat_plur ": Number_dat_plur, # bq, U,
    "Number_erg_sing ": Number_erg_sing, # bq, U,
    "Number_erg_plur ": Number_erg_plur, # bq, U,
    "Number_psee_sing ": Number_psee_sing, # U,
    "Number_psee_plur ": Number_psee_plur, # U,
    "Number_psor_sing ": Number_psor_sing, # cz, fi, sl, U,
    "Number_psor_plur ": Number_psor_plur, # cz, fi, sl, U,
    "NumForm_digit ": NumForm_digit, # cz, sl, U,
    "NumForm_roman ": NumForm_roman, # cz, sl, U,
    "NumForm_word ": NumForm_word, # cz, sl, U,
    "NumValue_one ": NumValue_one, # cz, U,
    "NumValue_two ": NumValue_two, # cz, U,
    "NumValue_three ": NumValue_three, # cz, U,
    "PartForm_pres ": PartForm_pres, # fi,
    "PartForm_past ": PartForm_past, # fi,
    "PartForm_agt ": PartForm_agt, # fi,
    "PartForm_neg ": PartForm_neg, # fi,
    "PartType_mod ": PartType_mod, # U,
    "PartType_emp ": PartType_emp, # U,
    "PartType_res ": PartType_res, # U,
    "PartType_inf ": PartType_inf, # U,
    "PartType_vbp ": PartType_vbp, # U,
    "Person_abs_one ": Person_abs_one, # bq, U,
    "Person_abs_two ": Person_abs_two, # bq, U,
    "Person_abs_three ": Person_abs_three, # bq, U,
    "Person_dat_one ": Person_dat_one, # bq, U,
    "Person_dat_two ": Person_dat_two, # bq, U,
    "Person_dat_three ": Person_dat_three, # bq, U,
    "Person_erg_one ": Person_erg_one, # bq, U,
    "Person_erg_two ": Person_erg_two, # bq, U,
    "Person_erg_three ": Person_erg_three, # bq, U,
    "Person_psor_one ": Person_psor_one, # fi, U,
    "Person_psor_two ": Person_psor_two, # fi, U,
    "Person_psor_three ": Person_psor_three, # fi, U,
    "Polite_inf ": Polite_inf, # bq, U,
    "Polite_pol ": Polite_pol, # bq, U,
    "Polite_abs_inf ": Polite_abs_inf, # bq, U,
    "Polite_abs_pol ": Polite_abs_pol, # bq, U,
    "Polite_erg_inf ": Polite_erg_inf, # bq, U,
    "Polite_erg_pol ": Polite_erg_pol, # bq, U,
    "Polite_dat_inf ": Polite_dat_inf, # bq, U,
    "Polite_dat_pol ": Polite_dat_pol, # bq, U,
    "Prefix_yes ": Prefix_yes, # U,
    "PrepCase_npr ": PrepCase_npr, # cz,
    "PrepCase_pre ": PrepCase_pre, # U,
    "PunctSide_ini ": PunctSide_ini, # U,
    "PunctSide_fin ": PunctSide_fin, # U,
    "PunctType_peri ": PunctType_peri, # U,
    "PunctType_qest ": PunctType_qest, # U,
    "PunctType_excl ": PunctType_excl, # U,
    "PunctType_quot ": PunctType_quot, # U,
    "PunctType_brck ": PunctType_brck, # U,
    "PunctType_comm ": PunctType_comm, # U,
    "PunctType_colo ": PunctType_colo, # U,
    "PunctType_semi ": PunctType_semi, # U,
    "PunctType_dash ": PunctType_dash, # U,
    "Style_arch ": Style_arch, # cz, fi, U,
    "Style_rare ": Style_rare, # cz, fi, U,
    "Style_poet ": Style_poet, # cz, U,
    "Style_norm ": Style_norm, # cz, U,
    "Style_coll ": Style_coll, # cz, U,
    "Style_vrnc ": Style_vrnc, # cz, U,
    "Style_sing ": Style_sing, # cz, U,
    "Style_expr ": Style_expr, # cz, U,
    "Style_derg ": Style_derg, # cz, U,
    "Style_vulg ": Style_vulg, # cz, U,
    "Style_yes ": Style_yes, # fi, U,
    "StyleVariant_styleShort ": StyleVariant_styleShort, # cz,
    "StyleVariant_styleBound ": StyleVariant_styleBound, # cz, sl,
    "VerbType_aux ": VerbType_aux, # U,
    "VerbType_cop ": VerbType_cop, # U,
    "VerbType_mod ": VerbType_mod, # U,
    "VerbType_light ": VerbType_light, # U,
}


NAMES = [key for key, value in sorted(IDS.items(), key=lambda item: item[1])]
