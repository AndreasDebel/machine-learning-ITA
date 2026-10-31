# Final report - Titanic

## A) At lære data og problem at kende

### 1. Hvilken type machine learning-problem er der tale om?

Det er **supervised learning** (overvåget læring) og mere præcist **binær klassifikation**.

- **Supervised:** Hver passager i datasættet har et kendt facit (overlevede eller døde), så modellen kan lære af data med labels.
- **Klassifikation, ikke regression:** `Survived` er ikke et tal på en skala, men en af få kategorier. Værdierne 0 og 1 er kun betegnelser for kategorierne.
- **Binær:** Der er to kategorier: 0 = døde, 1 = overlevede.

### 2. Hvor mange forskellige features er der (uden labels)?

**9 features:** `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin` og `Embarked`.

`PassengerId` og `Name` er kun identifikation, og `Survived` er det, der skal forudsiges, så ingen af dem tæller med.

### 3. Hvor mange features består Y-data (labels) af?

**Én**, nemlig `Survived` (0 = døde, 1 = overlevede), fordi vi kun forudsiger overlevelse og intet andet.

## B) Rensning af data

### Rækkefølge af trinene

Alle trin undtagen 3 og 4 ligger i `clean.py`, trin 3 i `correlation.ipynb`; `titanic.py` indeholder kun modellen.
Datafilerne er beskrevet i `data/INDEX.md`.

1. **Ret fejl i data:** 98 `Fare`-værdier uden decimalkomma divideres med 1000.
2. **Konvertér tekst til tal:** `Sex` → 0/1; den ene manglende `Embarked` udfyldes med `S`, og `Embarked` one-hot
   encodes. Desuden tilføjes `Age_missing` (0/1). Resultat: `titanic_800_cleaned.csv` med alle features.
3. **Undersøg sammenhængen mellem hver feature og overlevelse** med korrelation og grafer. Det er belægget for trin 4.
4. **Beslut hvilke features der fjernes**, og begrund hvorfor de ikke påvirker overlevelse.
5. **Fjern de valgte features**, så de hverken indgår i trænings- eller testdata. Resultat: `titanic_800_model.csv`.
6. **Opdel i trænings- og testsæt:** 640/160 (80/20), stratificeret på `Survived`, fast `random_state`.
7. **Udfyld manglende `Age`** med medianen fra træningssættet.
8. **Skalér** `Pclass`, `Age` og `Fare` med `StandardScaler` (gennemsnit 0, standardafvigelse 1). 0/1-kolonnerne
   skaleres ikke. Resultat: `titanic_800_train.csv` og `titanic_800_test.csv`.

Opgaveteksten siger, at der skaleres *før* opdelingen. Her fittes skaleringen og udfyldningsværdien for `Age` i stedet
kun på træningssættet og anvendes derefter på testsættet, så information fra testsættet ikke lækker ind i træningen.
Derfor sker trin 7 og 8 efter opdelingen.

### Fejl i `Fare`: manglende decimalkomma

**Hvad:** 98 af de 800 værdier i `Fare` er langt for høje, fx `7925` og `262375`. Den dyreste billet på Titanic kostede
ca. 512, og alle de forkerte værdier ligger over 6.900, så der er et tydeligt skel mellem rigtige og forkerte værdier.
Fejlen findes allerede i den udleverede fil fra Canvas.

**Hvorfor det er en fejl:** De forkerte værdier følger samme mønster. De svarer alle til billetpriser med præcis tre
decimaler, hvor punktummet er forsvundet (`7.925` → `7925`, `262.375` → `262375`). Alle 98 ender på 5, og ingen af de
korrekte priser har tre decimaler. Priser med færre eller flere decimaler (`7.25`, `71.2833`) er intakte. En sandsynlig
årsag er dansk talformat, hvor punktum bruges som tusindtalsseparator, så `7.925` er blevet læst som 7925.

**Hvorfor det skal rettes:** Uden rettelse bliver gennemsnitsprisen ca. 4.285 i stedet for ca. 33. Det ødelægger både
analysen af sammenhængen mellem pris og overlevelse og skaleringen, fordi nogle få ekstreme værdier dominerer.

**Hvordan:** Alle værdier over 600 divideres med 1000 (i `clean.py`). Bagefter ligger alle priser mellem 0 og 512,33,
og medianprisen er ca. 63 / 14,5 / 8 for 1. / 2. / 3. klasse, hvilket er realistisk. De 12 billetter med prisen 0 er
bevaret, da de er plausible.

### Valg af features

Valget bygger på korrelationen med `Survived` og graferne i `correlation.ipynb`. **Beholdes:** `Sex`, `Pclass`, `Age`,
`Fare` og `Embarked`. **Fjernes:** `SibSp`, `Parch`, `Ticket` og `Cabin`.

`Sex` har den stærkeste sammenhæng (korrelation 0,55; positiv, fordi kvinder er kodet som 1, så kvinder overlevede
oftere end mænd) og hænger kun svagt sammen med de andre features, så den tilfører information, som ingen anden feature
dækker. `Pclass` har også en stærk sammenhæng (−0,33): jo bedre klasse, jo større overlevelse. Fortegnet er negativt,
fordi den bedste klasse har nummer 1. Klassen hænger tæt sammen med billetpris, kahyt og billetnummer og kan til dels
repræsentere dem. `Fare` beholdes alligevel (korrelation 0,25), fordi overlapningen med `Pclass` kun er delvis (−0,56):
priserne varierer meget inden for samme klasse, og det er risikabelt at fjerne en feature med tydelig sammenhæng. `Age`
har en svag korrelation (−0,09), men sammenhængen er ikke lineær: de yngste børn overlevede markant oftere end
gennemsnittet, og overlevelsen falder for de ældste (dog få passagerer over 60). `Embarked` beholdes, fordi havnene
hænger tydeligere sammen med overlevelse end `SibSp` og `Parch`: Cherbourg (`Embarked_C`) har en positiv korrelation
(0,15) og Southampton (`Embarked_S`) en negativ (−0,14).

`SibSp` (−0,03) og `Parch` (0,08) fjernes på grund af meget lav korrelation. Manglende korrelation garanterer ikke, at en
feature er uden betydning, da der kan være ikke-lineære sammenhænge eller samspil med andre features, men her vælges en
enklere model. `Ticket` fjernes, fordi billetnummeret er svært at fortolke, næsten er unikt pr. passager (625 forskellige
værdier for 800 passagerer) og hænger sammen med klasse, kahyt og havn. `Cabin` fjernes, fordi den primært afspejler
klassen, og 615 af 800 værdier (77 %) mangler. `PassengerId` og `Name` indgår ikke, da de kun er identifikation.

### Manglende data

**`Age`** mangler for 163 af 800 passagerer (20 %). Der er tre muligheder: fjerne kolonnen, fjerne rækkerne eller
udfylde værdierne. Kolonnen beholdes, fordi alder har betydning for overlevelse (de yngste børn overlevede markant
oftere). Rækkerne beholdes, fordi det ville koste en femtedel af data, og især fordi de 163 passagerer ikke er en
tilfældig gruppe: de overlevede sjældnere end resten (30,1 % mod 40,7 %, udskrevet af `clean.py`). Uden dem ville
træningsdata give et for optimistisk billede, og modellen ville lære et skævt mønster.

Værdierne udfyldes derfor med **medianen** fra træningssættet (29 år). Medianen er valgt frem for gennemsnittet, fordi
den ikke trækkes af skæve fordelinger og ekstreme værdier; for `Age` er forskellen dog lille (median 28, gennemsnit 29,9
i hele datasættet). Udfyldning har en pris: 163 passagerer får samme opdigtede alder, hvilket udvisker aldersmønsteret
lidt. Derfor tilføjes en ny feature, **`Age_missing`** (1 = alderen manglede), så modellen kan skelne rigtige aldre fra
udfyldte og stadig bruge, at manglende alder hænger sammen med lavere overlevelse.

**`Embarked`** mangler for 1 passager (PassengerId 62) og udfyldes med den hyppigste havn, `S` (Southampton). Det
stemmer i øvrigt med de historiske kilder.

Medianen for `Age` beregnes kun på træningssættet og bruges derefter på testsættet, så testdata ikke påvirker
træningen. `Embarked` udfyldes før opdelingen, men `S` er den hyppigste havn med stor margin (577 af 800), så resultatet
er det samme uanset opdeling.

### Tekst til tal

`Sex` omkodes til 1 (kvinde) og 0 (mand). `Embarked` omkodes med **one-hot encoding**: hver havn får sin egen 0/1-kolonne
(`Embarked_C`, `Embarked_Q`, `Embarked_S`). Havnene har ingen naturlig rækkefølge, så en kodning som S/C/Q → 0/1/2 ville
give modellen en falsk rækkefølge at lære af.

### Opdeling i trænings- og testsæt

Data opdeles 80/20: 640 rækker til træning og 160 til test, som i kursets Titanic-øvelse (uge 6). Det er en
tommelfingerregel, ikke en matematisk optimal værdi: 640 rækker giver modellen nok eksempler at lære af, og 160
testrækker gør scoren stabil nok til at stole på (én forkert forudsigelse flytter nøjagtigheden 0,6 procentpoint).
Opdelingen er stratificeret på `Survived`, så andelen af overlevende er den samme i begge sæt (38,4 % og 38,8 %), og
den bruger et fast `random_state`, så den er ens ved hver kørsel.

### Skalering

`Pclass`, `Age` og `Fare` skaleres med `StandardScaler`, så hver kolonne får gennemsnit 0 og standardafvigelse 1. En
værdi angiver derefter, hvor mange standardafvigelser den ligger fra gennemsnittet. Uden skalering ville `Fare` (værdier
op til 512) dominere `Pclass` (1-3) i modeller, der sammenligner passagerer via afstande eller vægte, alene fordi tallene
er større.

`StandardScaler` er valgt som i kursets Titanic-øvelse (uge 6) og frem for min-max-skalering (0-1), fordi den håndterer
de få meget dyre billetter bedre: med min-max ville den dyreste billet (512) sætte skalaen, så næsten alle andre priser
blev klemt sammen mellem 0 og 0,12. 0/1-kolonnerne (`Sex`, `Age_missing`, `Embarked_*`) skaleres ikke, da de allerede
ligger på en sammenlignelig skala, og `Survived` skaleres ikke, da den er label. Skaleringen fittes kun på
træningssættet. Træbaserede modeller som random forest påvirkes ikke af skalering, men den gør det muligt at
sammenligne med andre modeller.

## C) Valg af model og træning

**Valg:** Et **decision tree**. Modeltypen er valgt ud fra data og opgaven, ikke ud fra målte resultater.

**Hvorfor decision tree:**

- **Passer til data:** Datasættet er en lille tabel, og overlevelse fulgte sandsynligvis regellignende mønstre
  ("kvinder og børn først"). Et træ arbejder netop med ja/nej-spørgsmål, fx om `Sex` eller `Age`.
- **Fanger samspil:** Betydningen af køn afhænger sandsynligvis af klassen. Et træ kan håndtere det uden hjælp, fordi
  hvert spørgsmål stilles inden for den gruppe, de tidligere spørgsmål har dannet.
- **Kan forklares:** Man kan følge en passager gennem træet og se præcis, hvorfor forudsigelsen blev, som den blev.

**Kendte svagheder:** Et træ kan overfitte og er følsomt over for små ændringer i træningsdata. Overfitting begrænses
med `max_depth`, og i sektion E er det planen at sammenligne med en **random forest**, der gennemsnitter mange træer og
derfor er mere stabil. Rækkefølgen følger kursets råd om at starte simpelt, og E bliver dermed en konkret test af, om
mange træer slår ét.

**Valg af dybde:** `max_depth` vælges med 5-fold krydsvalidering på træningssættet: de 640 rækker deles i fem dele, og
hver del bruges én gang til validering, mens træet trænes på de fire andre. Testsættet bruges ikke, så det forbliver en
ærlig slutmåling. Valget falder på den simpleste dybde, hvis score ligger inden for én standardafvigelse af den bedste:
den bedste er dybde 8 med 81,6 % (±0,8), så grænsen er 80,8 %, og **dybde 5** (80,9 %) er den simpleste, der når den.
Dybderne 3-8 ligger dog så tæt, at valget i praksis er et skøn og ikke et præcist resultat.

Træningsnøjagtigheden indgår ikke i valget, men bruges som kontrol. Ved dybde 5 er den 86,3 %, 5,4 point over
krydsvalideringen, mod 10,3 point ved dybde 8. Lave scores på begge mål ville betyde, at træet er for simpelt. Et træ
uden dybdegrænse når derimod 98,9 % på træningsdata, men kun 77,3 % i krydsvalidering: det har lært træningsdata udenad
i stedet for generelle mønstre.

Det endelige træ trænes derefter på alle 640 rækker med `max_depth=5`.

**Fravalgt:**

- **Logistisk regression:** enkel og forklarlig, men fanger kun samspil, hvis de tilføjes manuelt.
- **SVM:** kan fange samspil med en kernel, men er sværere at forklare.
- **Random forest:** mere stabil, men sværere at forklare end ét træ. Gemmes til sektion E.
- **MLP (neuralt netværk):** kursets model i Titanic-øvelsen (uge 6), men svær at forklare og med mange tal at lære
  (153 ved `(8,8)`) ud fra kun 640 passagerer.

## Skal nævnes i den endelige rapport (1 side)

- [ ] Hvorfor Titanic er valgt frem for Supply Chain (krav i opgaven).
- [ ] A: Supervised, binær klassifikation; 9 features, 1 label (`Survived`).
- [ ] B: Fejlen i `Fare` (98 værdier uden decimalkomma) og rettelsen (÷ 1000). Kort: 2-3 sætninger.
- [ ] B: Valg af features med belæg fra `correlation.ipynb` (se "Valg af features"). Kort i rapporten.
- [ ] B: Håndtering af manglende data: `Age` → træningsmedian + `Age_missing`-flag; `Embarked` → `S` (se "Manglende data").
- [ ] B: Tekst til tal (`Sex` → 0/1, `Embarked` → one-hot; se "Tekst til tal").
- [ ] B: Opdeling i trænings-/testsæt med begrundelse for størrelserne: 80/20 (640/160), stratificeret, fast `random_state` (se `decisions.md`).
- [ ] B: Skalering med `StandardScaler` af `Pclass`, `Age`, `Fare` (se "Skalering"); skalering og udfyldning fittes kun
  på træningssættet (afviger bevidst fra opgavens rækkefølge, undgår datalæk).
- [ ] C: Valg af decision tree med begrundelse og fravalg (se "C) Valg af model og træning").
- [ ] C: `max_depth=5` valgt med krydsvalidering på træningssættet; afstanden til træningsnøjagtigheden som kontrol (se "Valg af dybde").
- [ ] D-E: Evaluering og eksperimenter. *Ikke lavet endnu.*
