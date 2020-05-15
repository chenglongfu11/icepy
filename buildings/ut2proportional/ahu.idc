﻿;IDA 4.80002 Form UTF-8
(DOCUMENT-HEADER :TYPE SCHEMA :TITLE "CE Standard Air Handling Unit" :PAGE-WIDTH 177.5 :PAGE-HEIGHT 119) 
(CONNECTION-LINE :AT ((580 73) (688 73) (688 72)) :LINE-STYLE :DOT :FIRST-LINK ("Sched_AHU" (1.0 0.531) OUTSIGNALLINK) :LAST-LINK (:SELF 2.91 "Air_Ctrl") :DIR :RIGHT :ARROW (19 8)) 
(TEXT-OBJECT :VALUE (:DICT (ICE AHU CONST-TEMP-C)) :FONT (:SWISS :ARIAL 11 0) :AT ((40 80) (94 111)) :STYLE LABEL) 
(CONNECTION-LINE :AT ((563 258) (606 258)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("cc" (1 0.458) AIRFLOWOUT) :LAST-LINK ("sf" (0 0.458) FANIN) :EDGE 1) 
(CONNECTION-LINE :AT ((445 258) (509 258)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("hc" (1 0.458) AIRFLOWOUT) :LAST-LINK ("cc" (0 0.458) AIRFLOWIN) :EDGE 1) 
(CONNECTION-LINE :AT ((165 311) (192 311)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("AirExhaustRef" (0.948 0.5) LINK) :LAST-LINK ("rf" (0 0.458) FANOUT) :DIR :RIGHT :ARROW (19 8 8) :EDGE 1) 
(CONNECTION-LINE :AT ((158 258) (229 258) (293 258)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("AirSupplyRef" (0.938 0.5) LINK) :LAST-LINK ("hx" (0 0.081) SUPIN) :DIR :RIGHT :ARROW (19 8 8) :EDGE 1) 
(CONNECTION-LINE :AT ((658 258) (688 258)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("sf" (1 0.458) FANOUT) :LAST-LINK (:SELF 2.34 "Air_Sup") :EDGE 1) 
(TEXT-OBJECT :VALUE (GERMAN "Lüftungsgerät mit unbegrenzter Kapazität (als Vorgabe). Zulufttemperatur ist entweder (1) Konstant, (2) nach Zeitplan (3) in Abhängigkeit von der Außentemperatur.
Komponenten enthalten weitere veränderbare Parameter." ENGLISH "AHU with (by default) unlimited capacity. Supply air temperature setpoint is either (a) constant, (b) according to a time schedule or (c) a function of outside air temperature.

Additional parameters can be set by opening AHU components." FINNISH "IV-kone rajoittamattomalla teholla (oletus). Tuloilmavirran lämpötilan asetusarvo on joko (a) vakio, (b) aikataulutettu tai (c) ulkoilman lämpötilan funktio.

Lisäparametrit voidaan asettaa avaamalla IV-koneen komponentteja." FRENCH "CTA avec capacité illimitée (par défaut). Valeur de consigne de la température d’air fourni (a) constante, (b) selon une horaire ou (c) une fonction de la température de l’air extérieure.

Les paramètres additionnels peuvent être établis en ouvrant les composants de la CTA." SWEDISH "LB med (som standard) obegränsad kapacitet. Tilluftstemperaturens börvärde är antingen (a) konstant, (b) enligt ett tidsschema eller (c) beroende på utomhustemperaturen.

Ytterligare inställningar kan göras genom att öppna komponenterna i LB." SPANISH "UTA con (por defecto) capacidad ilimitada. El punto de consigna de la temperatura del aire de suministro es (a) constante, (b) según un horario(c) una función de la temperatura del aire exterior.

Los parámetros adicionales pueden ser establecidos abriendo los componentes de la UTA .") :AT ((12 384) (330 456)) :STYLE NOTE :LINE-GROUND #S(RGB RED 255 GREEN 255 BLUE 233) :OUTLINED-P T :MARKUP HTML :PADDING 5) 
(CONNECTION-LINE :AT ((343 311) (688 311)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("hx" (1 0.906) EXHIN) :LAST-LINK (:SELF 2.176 "Air_Rtn") :EDGE 1) 
(CONNECTION-LINE :AT ((344 258) (370 258) (393 258)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("hx" (1 0.078) SUPOUT) :LAST-LINK ("hc" (0 0.458) AIRFLOWIN) :EDGE 1) 
(CONNECTION-LINE :AT ((166 95) (181 95) (181 138) (221 138)) :LINE-STYLE :DOT :FIRST-LINK ("SupConst" (1 0.5) LINK) :LAST-LINK ("SupSwitch" (0.0 0.125) (INSIGNALLINK 1)) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((148 129) (166 129) (166 154) (220 154)) :LINE-STYLE :DOT :FIRST-LINK ("SupSchedule" (1.0 0.531) OUTSIGNALLINK) :LAST-LINK ("SupSwitch" (0 0.525) (INSIGNALLINK 2)) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((150 167) (184 167) (184 167) (221 167)) :LINE-STYLE :DOT :FIRST-LINK ("SupSetpoint" (1 0.576) OUTSIGNALLINK) :LAST-LINK ("SupSwitch" (0.0 0.85) (INSIGNALLINK 3)) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((70 173) (70 167) (100 167)) :FIRST-LINK ("TAmbRef" (0.5 0.0) LINK) :LAST-LINK ("SupSetpoint" (0 0.576) INSIGNALLINK) :DIR :RIGHT :ARROW (19 8 8)) 
(TEXT-OBJECT :VALUE (ENGLISH "Standard air handling unit" FINNISH "Vakio IV-kone" GERMAN "Standard-Lüftungsgerät" FRENCH "Unité de traitement d’air" SWEDISH "Standard luftbehandlingsaggregat" SPANISH "Unidad de tratamiento de aire estándar") :TEXT-COLOR :DEFAULT :FONT (:SWISS :ARIAL 16 1) :AT ((16 12) (379 32)) :STYLE SECTION) 
(EQUATION-FRAME :AT ((352 440)) :R (13.5 14) :ICON "lib:emeter.ids" :SLOT ("EmeterHeat") :NAME "EmeterHeat" :PADDING 3 :DATA :CEO) 
(EQUATION-FRAME :AT ((386 440)) :R (13.5 14) :ICON "lib:emeter.ids" :SLOT ("EmeterCool") :NAME "EmeterCool" :PADDING 3 :DATA :CEO) 
(LINK-FRAME :AT ((79 248) (163 268)) :STYLE HYPERLINK :SLOT (:SYSTEM CLIMATE AIRSUPPLY) :NAME "AirSupplyRef" :LABEL "AirSupply" :ICON CLIMATE-PIXMAP :DATA REFERENCE) 
(CONNECTION-LINE :AT ((296 76) (308 76) (308 114) (241 114) (241 134)) :LINE-STYLE :DOT :FIRST-LINK (AIR-SUPPLY-STRATEGY (1 0.5) LINK) :LAST-LINK ("SupSwitch" (0.5 0.01) SELECTORLINK) :DIR :RIGHT :ARROW (19 8 8)) 
(LINK-FRAME :AT ((38 173) (102 201)) :STYLE HYPERLINK :SLOT (:SYSTEM CLIMATE :VARIABLES TAIR2) :NAME "TAmbRef" :LABEL "TAir2" :SIDE :TOP :ICON CLIMATE-PIXMAP :DATA REFERENCE) 
(CONNECTION-LINE :AT ((428 73) (481 73) (481 207) (388 207) (271 207) (271 276) (293 276)) :LINE-STYLE :DOT :FIRST-LINK ("Sched_Vvx" 2.47 OUTSIGNALLINK) :LAST-LINK ("hx" (0 0.359) CONTROL) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((262 153) (294 153) (294 220) (550 220) (550 236)) :LINE-STYLE :DOT :FIRST-LINK ("SupSwitch" (1 0.5) OUTSIGNALLINK) :LAST-LINK ("cc" (0.792 0.0) TEMPSETPOINT)) 
(CONNECTION-LINE :AT ((262 153) (294 153) (294 220) (329 220) (433 220) (433 237)) :LINE-STYLE :DOT :FIRST-LINK ("SupSwitch" (1 0.5) OUTSIGNALLINK) :LAST-LINK ("hc" (0.792 0.025) TEMPSETPOINT)) 
(CONNECTION-LINE :AT ((262 153) (294 153) (294 220) (317 220) (317 251)) :LINE-STYLE :DOT :FIRST-LINK ("SupSwitch" (1 0.5) OUTSIGNALLINK) :LAST-LINK ("hx" (0.479 0) TEMPSETPOINT)) 
(CONNECTION-LINE :AT ((580 73) (675 73) (675 330) (258 330) (258 272) (201 272) (201 289)) :LINE-STYLE :DOT :FIRST-LINK ("Sched_AHU" (1.0 0.531) OUTSIGNALLINK) :LAST-LINK ("rf" (0.146 0.0) FANCONTROL) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((580 73) (649 73) (649 236)) :LINE-STYLE :DOT :FIRST-LINK ("Sched_AHU" (1.0 0.531) OUTSIGNALLINK) :LAST-LINK ("sf" (0.854 0.0) FANCONTROL) :DIR :RIGHT :ARROW (19 8 8)) 
(CONNECTION-LINE :AT ((544 283) (544 323) (544 323) (544 368)) :LINE-COLOR (:CALL PMT-COLOR [@ 1] [@ 2]) :LINE-STYLE 3 :FIRST-LINK ("cc" (0.667 0.983) LIQFLOWOUT) :LAST-LINK (:SELF 1.786 "AHU_Rtn_Cold")) 
(CONNECTION-LINE :AT ((519 283) (519 317) (519 317) (519 368)) :LINE-COLOR (:CALL PMT-COLOR [@ 1] [@ 2]) :LINE-STYLE 3 :FIRST-LINK ("cc" (0.15 0.983) LIQFLOWIN) :LAST-LINK (:SELF 1.749 "AHU_Sup_Cold")) 
(CONNECTION-LINE :AT ((427 283) (427 282) (427 282) (427 323) (427 368)) :LINE-COLOR (:CALL PMT-COLOR [@ 1] [@ 2]) :LINE-STYLE 3 :FIRST-LINK ("hc" (0.667 0.979) LIQFLOWOUT) :LAST-LINK (:SELF 1.61 "AHU_Rtn_Hot")) 
(CONNECTION-LINE :AT ((402 283) (402 319) (402 319) (402 368)) :LINE-COLOR (:CALL PMT-COLOR [@ 1] [@ 2]) :LINE-STYLE 3 :FIRST-LINK ("hc" (0.146 0.979) LIQFLOWIN) :LAST-LINK (:SELF 1.574 "AHU_Sup_Hot")) 
(CONNECTION-LINE :AT ((244 311) (244 311) (293 311) (293 311)) :LINE-COLOR #S(RGB RED 224 GREEN 224 BLUE 224) :LINE-GROUND #S(RGB RED 128 GREEN 128 BLUE 128) :LINE-STYLE 2 :FIRST-LINK ("rf" (1 0.458) FANIN) :LAST-LINK ("hx" (0 0.9) EXHOUT) :EDGE 1) 
(LINK-FRAME :AT ((74 301) (170 321)) :STYLE HYPERLINK :SLOT (:SYSTEM CLIMATE AIREXHAUST) :NAME "AirExhaustRef" :LABEL "AirExhaust" :ICON CLIMATE-PIXMAP :DATA REFERENCE) 
(EQUATION-FRAME :AT ((241 76)) :R (50 12) :ICON "sys:constant.ids" :SLOT (AIR-SUPPLY-STRATEGY) :TITLE "=(:$ :DICT (ICE AHU ASS-CAPTION))" :NAME AIR-SUPPLY-STRATEGY :DATA SOURCE-CONSTANT) 
(EQUATION-FRAME :AT ((128 95)) :R (34 10) :ICON "sys:constant.ids" :SLOT ("SupConst") :NAME "SupConst" :DATA SOURCE-CONSTANT) 
(SELF-FRAME :AT ((352 206)) :R (336 162) :SLOT (:SELF) :DATA MACRO-OBJECT) 
(FRAME-BOX :VALUE (:DICT (ICE AHU AIR-SUP-SETPT)) :AT ((34 56) (314 201)) :STYLE SECTION) 
(EQUATION-FRAME :AT ((124 128)) :R (24 16) :ICON "lib:schedule.ids" :SLOT ("SupSchedule") :NAME "SupSchedule") 
(EQUATION-FRAME :AT ((125 165)) :R (24 15.5) :ICON "lib:PLINSEGM.ids" :SLOT ("SupSetpoint") :NAME "SupSetpoint" :DATA :EO :HELP-STRING (:DICT (ICE AHU SUPSETPOINT))) 
(EQUATION-FRAME :AT ((241 153)) :R (20 20) :ICON "lib:nswitch.ids" :SLOT ("SupSwitch") :NAME "SupSwitch" :DATA :CEO) 
(EQUATION-FRAME :AT ((404 72)) :R (24 16) :ICON "lib:schedule.ids" :SLOT ("Sched_Vvx") :TITLE "=(:$ :DICT (ICE AHU HE-S-CAPTION))" :NAME "Sched_Vvx" :DATA SCHEDULE :HELP-STRING (:DICT (ICE EO SCHEDULE))) 
(EQUATION-FRAME :AT ((556 72)) :R (24 16) :ICON "lib:schedule.ids" :SLOT ("Sched_AHU") :TITLE "=(:$ :DICT (ICE AHU FAN-S-CAPTION))" :NAME "Sched_AHU" :DATA SCHEDULE :HELP-STRING (:DICT (ICE EO SCHEDULE))) 
(EQUATION-FRAME :AT ((386 404)) :R (13.5 14) :ICON "lib:emeter.ids" :SLOT ("EmeterFans") :NAME "EmeterFans" :PADDING 3 :DATA :CEO) 
(EQUATION-FRAME :AT ((352 404)) :R (13.5 14) :ICON "lib:emeter2.ids" :SLOT ("EmeterRecycle") :NAME "EmeterRecycle" :PADDING 3 :DATA :CEO) 
(EQUATION-FRAME :AT ((318 285)) :R (24 32) :SLOT ("hx") :NAME "hx" :DATA :EO :HELP-STRING (:DICT (ICE AHU HX))) 
(EQUATION-FRAME :AT ((419 260)) :R (24 24) :ICON "lib:HCSIMCTR.ids" :SLOT ("hc") :NAME "hc" :DATA :EO :HELP-STRING (:DICT (ICE AHU HC))) 
(EQUATION-FRAME :AT ((536 260)) :R (24 24) :ICON "lib:CCSIMCTR.ids" :SLOT ("cc") :NAME "cc" :DATA :EO :HELP-STRING (:DICT (ICE AHU CC))) 
(EQUATION-FRAME :AT ((632 260)) :R (24 24) :ICON "lib:CEFAN.ids" :SLOT ("sf") :NAME "sf" :DATA :EO :HELP-STRING (:DICT (ICE AHU SF))) 
(EQUATION-FRAME :AT ((218 313)) :R (24 24) :ICON "lib:CEFAN.ids" :SYMMETRY (180.0) :SLOT ("rf") :NAME "rf" :DATA :EO :HELP-STRING (:DICT (ICE AHU RF))) 
(FRAME-BOX :VALUE (:DICT (GENERAL RESULTS)) :AT ((404 384) (687 456)) :STYLE SECTION :LINE-COLOR #S(RGB RED 33 GREEN 33 BLUE 192)) 
(LIST-FIELD :AT ((408 392) (678 448)) :SLOT (:RESULTS) :TEXT-COLOR #S(RGB RED 0 GREEN 0 BLUE 0)) 