from cymem.cymem cimport Pool
from preshed.maps cimport PreshMapArray
from libc.stdint cimport uint64_t

from .structs cimport TokenC
from .strings cimport StringStore
from .typedefs cimport attr_t
from .parts_of_speech cimport univ_pos_t

from . cimport symbols

cdef struct RichTagC:
    uint64_t morph
    int id
    univ_pos_t pos
    attr_t name


cdef struct MorphAnalysisC:
    RichTagC tag
    attr_t lemma


cdef class Morphology:
    cdef readonly Pool mem
    cdef readonly StringStore strings
    cdef public object lemmatizer
    cdef readonly object tag_map
    cdef public object n_tags
    cdef public object reverse_index
    cdef public object tag_names

    cdef RichTagC* rich_tags
    cdef PreshMapArray _cache

    cdef int assign_tag(self, TokenC* token, tag) except -1

    cdef int assign_tag_id(self, TokenC* token, int tag_id) except -1
    
    cdef int assign_feature(self, uint64_t* morph, feature, value) except -1


cpdef enum univ_morph_t:
    NIL = 0
    Animacy_anim = symbols.Animacy_anim
    Animacy_inam
    Aspect_freq
    Aspect_imp
    Aspect_mod
    Aspect_none
    Aspect_perf
    Case_abe
    Case_abl
    Case_abs
    Case_acc
    Case_ade
    Case_all
    Case_cau
    Case_com
    Case_dat
    Case_del
    Case_dis
    Case_ela
    Case_ess
    Case_gen
    Case_ill
    Case_ine
    Case_ins
    Case_loc
    Case_lat
    Case_nom
    Case_par
    Case_sub
    Case_sup
    Case_tem
    Case_ter
    Case_tra
    Case_voc
    Definite_two
    Definite_def
    Definite_red
    Definite_ind
    Degree_cmp
    Degree_comp
    Degree_none
    Degree_pos
    Degree_sup
    Degree_abs
    Degree_com
    Degree_dim # du
    Gender_com
    Gender_fem
    Gender_masc
    Gender_neut
    Mood_cnd
    Mood_imp
    Mood_ind
    Mood_n
    Mood_pot
    Mood_sub
    Mood_opt
    Negative_neg
    Negative_pos
    Negative_yes
    Number_com
    Number_dual
    Number_none
    Number_plur
    Number_sing
    Number_ptan # bg
    Number_count # bg
    NumType_card
    NumType_dist
    NumType_frac
    NumType_gen
    NumType_mult
    NumType_none
    NumType_ord
    NumType_sets
    Person_one
    Person_two
    Person_three
    Person_none
    Poss_yes
    PronType_advPart
    PronType_art
    PronType_default
    PronType_dem
    PronType_ind
    PronType_int
    PronType_neg
    PronType_prs
    PronType_rcp
    PronType_rel
    PronType_tot
    PronType_clit
    PronType_exc # es, ca, it, fa
    Reflex_yes
    Tense_fut
    Tense_imp
    Tense_past
    Tense_pres
    VerbForm_fin
    VerbForm_ger
    VerbForm_inf
    VerbForm_none
    VerbForm_part
    VerbForm_partFut
    VerbForm_partPast
    VerbForm_partPres
    VerbForm_sup
    VerbForm_trans
    VerbForm_gdv # la
    Voice_act
    Voice_cau
    Voice_pass
    Voice_mid # gkc
    Voice_int # hb
    Abbr_yes # cz, fi, sl, U
    AdpType_prep # cz, U
    AdpType_post # U
    AdpType_voc # cz
    AdpType_comprep # cz
    AdpType_circ # U
    AdvType_man
    AdvType_loc
    AdvType_tim
    AdvType_deg
    AdvType_cau
    AdvType_mod
    AdvType_sta
    AdvType_ex
    AdvType_adadj
    ConjType_oper # cz, U
    ConjType_comp # cz, U
    Connegative_yes # fi
    Derivation_minen # fi
    Derivation_sti # fi
    Derivation_inen # fi
    Derivation_lainen # fi
    Derivation_ja # fi
    Derivation_ton # fi
    Derivation_vs # fi
    Derivation_ttain # fi
    Derivation_ttaa # fi
    Echo_rdp # U
    Echo_ech # U
    Foreign_foreign # cz, fi, U
    Foreign_fscript # cz, fi, U
    Foreign_tscript # cz, U
    Foreign_yes # sl
    Gender_dat_masc # bq, U
    Gender_dat_fem # bq, U
    Gender_erg_masc # bq
    Gender_erg_fem # bq
    Gender_psor_masc # cz, sl, U
    Gender_psor_fem # cz, sl, U
    Gender_psor_neut # sl
    Hyph_yes # cz, U
    InfForm_one # fi
    InfForm_two # fi
    InfForm_three # fi
    NameType_geo # U, cz
    NameType_prs # U, cz
    NameType_giv # U, cz
    NameType_sur # U, cz
    NameType_nat # U, cz
    NameType_com # U, cz
    NameType_pro # U, cz
    NameType_oth # U, cz
    NounType_com # U
    NounType_prop # U
    NounType_class # U
    Number_abs_sing # bq, U
    Number_abs_plur # bq, U
    Number_dat_sing # bq, U
    Number_dat_plur # bq, U
    Number_erg_sing # bq, U
    Number_erg_plur # bq, U
    Number_psee_sing # U
    Number_psee_plur # U
    Number_psor_sing # cz, fi, sl, U
    Number_psor_plur # cz, fi, sl, U
    NumForm_digit # cz, sl, U
    NumForm_roman # cz, sl, U
    NumForm_word # cz, sl, U
    NumValue_one # cz, U
    NumValue_two # cz, U
    NumValue_three # cz, U
    PartForm_pres # fi
    PartForm_past # fi
    PartForm_agt # fi
    PartForm_neg # fi
    PartType_mod # U
    PartType_emp # U
    PartType_res # U
    PartType_inf # U
    PartType_vbp # U
    Person_abs_one # bq, U
    Person_abs_two # bq, U
    Person_abs_three # bq, U
    Person_dat_one # bq, U
    Person_dat_two # bq, U
    Person_dat_three # bq, U
    Person_erg_one # bq, U
    Person_erg_two # bq, U
    Person_erg_three # bq, U
    Person_psor_one # fi, U
    Person_psor_two # fi, U
    Person_psor_three # fi, U
    Polite_inf # bq, U
    Polite_pol # bq, U
    Polite_abs_inf # bq, U
    Polite_abs_pol # bq, U
    Polite_erg_inf # bq, U
    Polite_erg_pol # bq, U
    Polite_dat_inf # bq, U
    Polite_dat_pol # bq, U
    Prefix_yes # U
    PrepCase_npr # cz
    PrepCase_pre # U
    PunctSide_ini # U
    PunctSide_fin # U
    PunctType_peri # U
    PunctType_qest # U
    PunctType_excl # U
    PunctType_quot # U
    PunctType_brck # U
    PunctType_comm # U
    PunctType_colo # U
    PunctType_semi # U
    PunctType_dash # U
    Style_arch # cz, fi, U
    Style_rare # cz, fi, U
    Style_poet # cz, U
    Style_norm # cz, U
    Style_coll # cz, U
    Style_vrnc # cz, U
    Style_sing # cz, U
    Style_expr # cz, U
    Style_derg # cz, U
    Style_vulg # cz, U
    Style_yes # fi, U
    StyleVariant_styleShort # cz
    StyleVariant_styleBound # cz, sl
    VerbType_aux # U
    VerbType_cop # U
    VerbType_mod # U
    VerbType_light # U


