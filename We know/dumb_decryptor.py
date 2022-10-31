#a b c d e f g h i j k l m n o p q r s t u v w x y z
#n o p q r s t u v w x y z a b c d e f g h i j k l m                             
txt = "Terrgvatf, arjpbzre! Jr ner tynq gb frr, gung lbh unir fhpprffshyyl cnffrq bhe vavgvny grfg. Qba'g or fb cebhq bs lbhefrys - vg'f whfg n grfg gb svygre zbfg hfryrff crbcyr, gung pna qb abguvat sbe bhe pbzzhavgl. Orsber jr jvyy cnff lbh fbzr erny gnfxf gb qb - chg lbhe rapelcgvba penpxre gb lbhe ercbfvgbel. Anzr sbyqre Jr xabj, naq chg vafvqr qhzo_qrpelcgbe.cl. Nyfb, va beqre gb cnff guvf gnfx - lbh fubhyq jevgr Dhvf phfgbqvrg vcfbf phfgbqrf nf n pbzzrag. Guvf zrffntr va pbzzrag frpgvba vf lbhe npprcgnapr sbe gur fbzr arj wbo gb qb. Jr ner jnvgvat..."
y = "abcdefghijklmnopqrstuvwxyz"
x = "nopqrstuvwxyzabcdefghijklm"
Translate = txt.maketrans(x, y)
print(txt.translate(Translate))