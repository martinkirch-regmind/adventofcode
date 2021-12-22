from functools import total_ordering
from heapq import *
from time import time

puzzle_input = """1839699672891217819841135688732885247928872185751688897193694689841978768898988716768379159626957769
2192965275394162996999895995785387868994994237879517119896718684447799929129197684778981358614968999
4927383925892593199621279935962919798987897179929239949761461388699843711988814644869741378719173483
8477219799114299945911696955298929578477221885481596518899422291833711899891919649968262899912978495
2817819315696246315613761896884311877197776956918937431899919989993647979687738979982159319969999578
3921996199497877997385372981891389397955538984319996184818154286982971629971788627117188715658844389
5696289699499785672395936877891787618217139792484279891873848972886677869648279849941981792717281246
7129788971966517941968791978867682499789996196627769926196599536999511916296719695918118513815976349
1381929498954922995835988798893531695699987868681872499899992886217921974289119956826999218123897213
3549913197832174177998998971454816159459558141919981479795995936196572194594817927979929738759867894
9611896297924264799116365948992848469239159938929996899929777915699853979918582424799771491998912979
8896967853332494975677896997672171389899888116469938368961869677885966598315829996195872879574939986
9626189338738929979981447485199177591878259393971396598363117898998298987485689289496613119256439899
2581156691693933978289919429717851359711529572527892887523428997945121976943613884281932582667716991
4857749547398635351971151567993497882693289669919191261189467927291485822988998937261939351941999294
9979549966583584768911191197888394588359811168955197992344559871917368365693995819623578492892117965
7917619899893818421929319482596212795441911115499449598578141584124868349823956298792992725966777516
2697478689842617698991751821916919179878699969168944195711127939671889181979689787352786387785699521
5628861417276569893927949572431986589991615467936891731193459939419453649317149915959852176399973589
8598569847167978841129794826999662765259922655959764477818121949594195739723999227684728927989339119
4182959939882942967265114769585986179935694989457955516994462933849599811279155619129418458797995622
1279595759999171395932712699994819257845174915367819726796291129129599651846687999276797388996427778
9296982979291838998696697779899683138299888951939184269574988996713891298254594788689192581761749199
7898529747921567799259614785195711298722899995563953389729854138375923998574978337182583278948847719
5759446778338982811699959831289965877558538939879994889218461796989951784178978799849671789158886897
7415595795257999869637399856813943916821952389724896878395719969295689189795989165918718449122987199
5277453841999959187658984456999172829279388688718797962891581393742197336462888178979189352184979949
5999981119718823799197782992389545832933319635165527477618193669683395899625211846978654499226399797
7322199138398291243793993699835559699138756292792984578118155756991829199928884365469898457139328686
9775914799619642898291963375991191628695225917979692891671897729899818377814699992599988648899942791
8948987951991949582694791597541537194826936836198728557871776596876483555677964781688292387914326753
9213756988419798972995796183793994111132948871779176579959128321249279918195586594789188299644117867
9988433162977618915986998165315738891899136974228444679817784196285989196833829498599242575681145814
9791592618881314992187289981991739796732996331271778166199345941317931346471829257789892157381499863
9499419789996969573941937888782528949789684318198482997994745339176219598921458631299916799778884817
2277686127357627956911728981267798224881752966899798581725971189337959769999869229925117426917625199
1999699745289281249967797888799871999146947533529539989233621472949571967151789691253813551194618681
9238952871919977668545861691928249849927594589174716439899152978859299629711884871697927912461472994
5693999942961769969718338296515799968282716963999984993888892242696899996795925781241445296217627178
8792428798344969728695853837168378997699984979131949839165699783857198193498498736992586279899821412
1341919577154536468492199645582852198865993428962991914182893729629689781488953997938479967399146778
9898949742669498817836927188698938227948751963788368618567158392937389662143188419869976976925878791
3863117255166859917114949882975512671793669888162298313911399221119869882291829638194582789793418289
9596288958978715572748999386778128882784799162918942799919631858671496234669281962991995233992749952
6997779116995311359832955891964599794272117296498929189987697599197694888589441578989117831993918718
7219931668741539419881791921297299193759485378719199131594468581498823119993138431698117329151685993
9991785795956519898724215929388399519198169893772269522781911299828828719913593119159389994321995377
1589752819788998863984993442776834999519338818989989495699398699154669871729719681765719291527179338
8677957657692461442138991259699913791937168914981686493768195739178827997898947526914998694258679922
4849917555929118828918968891876276887639893972978948923811398959691888936961558869619293798468841985
7591968777781688486657287185989899191971952213756197996811597477672998399939675983945724719698884599
6899888699478362939992989749759999712997799584666749322821376782881741755288569217947936871182976848
1735199974829194482981896378227633177972319179949967756755521733779617177179359212319773425697866997
3817786989897897994439614784549395537969388789791413599197191838485991439746959838499918989897373913
2719191794268958189883498885198299315552993614929981815887488991913575719125897648119198699694955658
8611179529935254458198327845291391389724392969973839397898842294993199375485515291996883222899689991
8398823979899558976479278944596967387155551118966181677313118773839682992993917222897269187917874592
2487941895917465999597918394945859695258999448375194788482811987238831113585754399697111268658668889
3165197318894179819982145518884339855547283986969388189465598238955334846398599126862329692958664948
3214872888941835551618295749815936447379164982127158756962916255229169362959926278166736999319912819
4868124598799489351953998942791869914281926889999798529189893579219896982989159757889999382997456943
8672278997992939676945791326494928981411855996524976679577219115682448991379182496989176176892955997
8111891278678128919594646897157998782266751249261774371581459924956699896849994366954445434474781578
8249786717337987789952959798892829877893399167892331184917262668179734459799489311239757879516294465
9852771579612566998897674385811911818948564954991939885767921923981188625619181137998899948258572979
8612233978552678659564598998421227845993777696273794576957923128579776275997368719911972768685865998
6396851886891895296969881984429869249152211913969992437536151582791889978657684752357197472254994988
3695799988814791969715781692449771636664975681917717875419692871833998897968137988438688312531982994
9799816699679961493172819538998439929815883179937897936513288991893517969173952292367191736769497839
5487189519289987929697958195599289891998858434678412995965929931628861499363469341795747195949193877
6739149655994322287114451851696968915518886882179199899799198896298439491168965677946959585791922991
7875868799175446444492125897984182249898398898198398899624194998968992755965526468819199935461896522
9923777354998999989529234613945179216797888819972843544155815189644616839788974886941699326421549841
9837752658678939554498959998869286695381999792678588829498726116797976874754432625959997899964961117
4717998192119995873889929597352494574179889139457687881597984631978122179999847756728256698191958875
1147792391878293969869927531466959648488946866744187478828598431946397869339996555913936372485598319
1729458969812991729853868291992796927589977318749959991121659524578882749876653191899888916983993938
5422297182981548376898998215962759232393984336464957894919858956974254531489959719997972873997937692
3199336788797284719839921695495517272991434711495852899631691933861734818967428219448778989968921925
3889221762999735892919139864989364219919169731157979281459579889482418486891595961949493447544517193
9355469915996928586767975877917345931266994986698979919796174258151191169995547961865818119648997268
8692788299949696166916297743985789626882949981798279977178688415833151985953312384733396838865784999
9316745159996983928757926544879899715977394193949854489942766891919251799289766868549937433785889914
9937295953918786961694665799391691269467721681791691569576999292476928869517976198997996715957887973
8999699441572871874518614611114944189659589819985946914755696873491986611733664565758846724456999784
9116981466999567259618817461965968995197895178699925761889819968695815843195626222889663978266638312
7496777622968979738689969982199115142999716676411153547457678983372187937369468776931919982541562956
9711218859281461218983199251368361768986916826888997785964293959998789268113318238149695966879999797
6396519733444912825295488769115364759158246882639423329569891881919222497434924659991959287999748365
3591978594781812551657193838674165375218922829899666689958499971985994795445889338599149989672551988
9162686192777939527739918151948819936589514481514772297919921699455894972279155835299769254289449518
8597167796744489859182666617666191913229499513732992789613684219819139687799191187969614489978432719
8725996361192474996782398367199589936642142186985992467978955321715239979857188349439928391129199188
9914982598239713756772933962271117962459258999596911828443669896324963789594196632987171698531997995
9292787327339152989498298698897892123859477919765998144995958191875619248199229793829439922998911971
7168891919118159796997743319856499417567997747972686299988494498485789859333169934997951999978853556
8961965298269611964877937134849653928898265888386915993799796699279138978121546916964914764987918881
9879861126679363918974986484928288831691848721349296732824948923888932696139779188699788579981817411
9537881896773448882931789856999511751189985796662931657323198877792797393599726994959993148693994398
8933595393747579247498891129685978923196761941162347892984592262912838443199289579117219188537241993"""

test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

my_input = """11199
99199
91189
91919
99911""" #expects mindist=16

risklevels = [[int(i) for i in line] for line in puzzle_input.split("\n")]
print(f"input size is {len(risklevels)},{len(risklevels[0])}")
base = len(risklevels)

def rotate(i, r):
    res = i + r
    if res >= 10:
        res = res % 10 + 1
    return res

for r in range(4):
    for i in range(base):
        for j in range(base):
            risklevels[i].append(rotate(risklevels[i][j], r + 1))

for r in range(4):
    for i in range(base):
        risklevels.append([rotate(risklevels[i][j], r + 1) for j in range(len(risklevels[i]))])

limit = len(risklevels)
print(f"complete input size: {limit}")

infinity = 999999999
known_shortest_distance = None

@total_ordering
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.risk = risklevels[x][y]
        self.dist = None
        self.best_dist_to_limit = infinity
        # best possible dist to the end:
        self.dist_to_limit = (limit - self.x) + (limit - self.y)
        self.is_in_potential = False

    def __eq__(self, __o: object) -> bool:
        return (isinstance(__o, Point)
            and __o.best_dist_to_limit == self.best_dist_to_limit
        )

    def __lt__(self, __o: object) -> bool:
        """
        sort by [current known distance to start] + [best possible dist to end]
        """
        return (isinstance(__o, Point)
            and self.best_dist_to_limit < __o.best_dist_to_limit
        )


dist = []
for i in range(limit):
    dist.append(list())
    for j in range(limit):
        dist[i].append(Point(i, j))

# "the starting position is never entered, so its risk is not counted"
dist[0][0].dist = 0
dist[0][0].risk = 0
potential = [dist[0][0]]
dist[0][0].is_in_potential = True

heapify_calls = 0

def maybe(x, y, current_dist):
    """
    adds a point to `append_to` if it's possible to go to (x,y) and if it's
    shorter than previously known path, assuming we're on a path of `current_dist`.
    """
    global heapify_calls
    if x < 0 or x >= limit or y < 0 or y >= limit:
        return
    point = dist[x][y]
    point_dist = point.dist
    potential_dist = current_dist + point.risk
    if not point_dist or potential_dist < point_dist:
        point.dist = potential_dist
        point.best_dist_to_limit = potential_dist + point.dist_to_limit
        if point.is_in_potential:
            heapify(potential)
            heapify_calls += 1
        else:
            heappush(potential, point)

start_t = time()

target = limit - 1
while potential:
    try:
        current = heappop(potential)
        current.is_in_potential = False
    except IndexError:
        break
    current_dist = current.dist
    if known_shortest_distance and dist and current.best_dist_to_limit > known_shortest_distance:
        continue
    maybe(current.x+1, current.y, current_dist)
    maybe(current.x-1, current.y, current_dist)
    maybe(current.x, current.y+1, current_dist)
    maybe(current.x, current.y-1, current_dist)
    if current.x == target and current.y == target:
        known_shortest_distance = current_dist
        print(f"best known_shortest_distance:{known_shortest_distance}")

# for i in range(limit):
#     print(dist[i][:limit])
print(dist[target][target].dist, ", took ", time()-start_t, "s")
print(f"called heapify {heapify_calls} times")

# wow, phase2 on test input goes straight to the best solution:
# 315 , took  0.01729750633239746 s
# called heapify 0 times
