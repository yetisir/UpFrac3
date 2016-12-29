mName = 'voronoiGranite'
sName = ['voronoiGranite(0.0)', 'voronoiGranite(0.1)', 'voronoiGranite(0.2)', 'voronoiGranite(0.3)']

abaqusMaterial = 'concreteDamage'
    
gridPoints = [[0, 0], [10, 0], [10, 10], [0, 10], [0, 0]]

sectionLocation = (10/2, 10/2, 0.0)

simulationTime = 100
numberOfSteps = 50

confiningStress = [500000.0, 1000000.0, 2000000.0, 4000000.0]

density = 2700.0
approxStrain = 0.05

boundaryDisplacements = [([(0.0, 0.0), (2.0, 0.005910598269275015), (4.0, 0.016220736276261014), (6.0, 0.030216945766756861), (8.0, 0.0471474805322568), (10.0, 0.06706722900481274), (12.0, 0.089430725858940449), (14.0, 0.11356599132872514), (16.0, 0.1398877831960223), (18.0, 0.17058711344331723), (20.0, 0.20666777002380721), (22.0, 0.24400923098617822), (24.0, 0.279516902834961), (26.0, 0.31700428669539737), (28.0, 0.36221998926429111), (30.0, 0.40892872338497027), (32.0, 0.46858758865785988), (34.0, 0.54303479583034187), (36.0, 0.59358703833658777), (38.0, 0.63853640237669929), (40.0, 0.6738176273089036), (42.0, 0.70866602869467332), (44.0, 0.74357516282405101), (46.0, 0.77691893566364867), (48.0, 0.80994668879138221), (50.0, 0.84637454374476007), (52.0, 0.88261973762735457), (54.0, 0.92042227717247971), (56.0, 0.96353953842152884), (58.0, 1.0097026794431763), (60.0, 1.0536565686385928), (62.0, 1.0987971944848447), (64.0, 1.1335069924566041), (66.0, 1.1763155804478203), (68.0, 1.219024610738729), (70.0, 1.2537612683087191), (72.0, 1.2914452253342672), (74.0, 1.322575731946666), (76.0, 1.3581253697999784), (78.0, 1.3946951359097501), (80.0, 1.4350603878078196), (82.0, 1.4717112836436113), (84.0, 1.5127636236870392), (86.0, 1.556702835644824), (88.0, 1.5930079096512137), (90.0, 1.6287452462598118), (92.0, 1.6676018010833606), (94.0, 1.6960997150746078), (96.0, 1.7296018628561387), (98.0, 1.7628237683372552), (100.0, 1.7993206609505987)], [(0.0, 0.0), (2.0, -0.0099130296277498003), (4.0, -0.019752432351288388), (6.0, -0.029527092659789603), (8.0, -0.039232874270534804), (10.0, -0.048819837125096348), (12.0, -0.058221720288094289), (14.0, -0.067434818425626791), (16.0, -0.076534055996409237), (18.0, -0.085175915951683112), (20.0, -0.093882649409633673), (22.0, -0.10254637683122293), (24.0, -0.11117123794566448), (26.0, -0.12060803437969976), (28.0, -0.1300687785154741), (30.0, -0.13999452833977438), (32.0, -0.15056949683123866), (34.0, -0.16270716419593689), (36.0, -0.17361401678848948), (38.0, -0.18218286812937426), (40.0, -0.1908463671411863), (42.0, -0.19947048803098752), (44.0, -0.20741973976982128), (46.0, -0.21489354604157823), (48.0, -0.22188593858957878), (50.0, -0.22930500368919113), (52.0, -0.23763223131459468), (54.0, -0.24553016632482311), (56.0, -0.25430965927951238), (58.0, -0.26274096933104363), (60.0, -0.27045684584484303), (62.0, -0.27707340195455371), (64.0, -0.27974037684295311), (66.0, -0.28693698346876545), (68.0, -0.29274332374733864), (70.0, -0.29484409938838319), (72.0, -0.30076375826458634), (74.0, -0.30759140257885853), (76.0, -0.3191202681147231), (78.0, -0.33148012619563577), (80.0, -0.33978542914493692), (82.0, -0.34693669970640334), (84.0, -0.35428012543974535), (86.0, -0.36134613664239446), (88.0, -0.36890555792830038), (90.0, -0.37688939537250588), (92.0, -0.38408614659725449), (94.0, -0.39138218190997576), (96.0, -0.39866980845934513), (98.0, -0.40586795347976218), (100.0, -0.41371044056506701)]), ([(0.0, 0.0), (2.0, 0.0048968230310938304), (4.0, 0.011914910669588899), (6.0, 0.021401059518355657), (8.0, 0.033007749344314261), (10.0, 0.046436336965045108), (12.0, 0.061589046889040835), (14.0, 0.07832685371046838), (16.0, 0.096129595556586747), (18.0, 0.11595238066414598), (20.0, 0.1371332793704311), (22.0, 0.15911842236294654), (24.0, 0.18230094016797971), (26.0, 0.20577224881319425), (28.0, 0.23078317280873989), (30.0, 0.25559225784712292), (32.0, 0.28779424656004765), (34.0, 0.32531538582181657), (36.0, 0.36652031995785622), (38.0, 0.40999327079133668), (40.0, 0.45448990801145756), (42.0, 0.49749897939318388), (44.0, 0.53519165912511157), (46.0, 0.61833187263536582), (48.0, 0.65303844783102427), (50.0, 0.69320195256387707), (52.0, 0.73321129696680198), (54.0, 0.77271246458098797), (56.0, 0.81209913937588196), (58.0, 0.84686148364346647), (60.0, 0.88802239167886388), (62.0, 0.93135596597995629), (64.0, 0.97921503308005076), (66.0, 1.0228475925960465), (68.0, 1.0695134672273114), (70.0, 1.1102058936753019), (72.0, 1.1449024376884318), (74.0, 1.184651002927932), (76.0, 1.2271242824897495), (78.0, 1.2729084319094299), (80.0, 1.3212907462744319), (82.0, 1.3626858704719782), (84.0, 1.4071397487130608), (86.0, 1.4478295777498733), (88.0, 1.4938846005515884), (90.0, 1.5341177083530886), (92.0, 1.5746503905854472), (94.0, 1.6036233961221353), (96.0, 1.6062917653503361), (98.0, 1.6997951521314756), (100.0, 1.73093434438251)], [(0.0, 0.0), (2.0, -0.0099743857458586688), (4.0, -0.019844827012812434), (6.0, -0.029694786901990653), (8.0, -0.03952904692911989), (10.0, -0.049362967631175619), (12.0, -0.059181712757597933), (14.0, -0.068941280341849362), (16.0, -0.078741454080098527), (18.0, -0.088394357084822489), (20.0, -0.098045137811224842), (22.0, -0.10761440302977267), (24.0, -0.11713417417918909), (26.0, -0.12624133844389474), (28.0, -0.1357874608130798), (30.0, -0.14519668372150507), (32.0, -0.15345567385134162), (34.0, -0.16112781616334529), (36.0, -0.16889785164753557), (38.0, -0.1769070466456274), (40.0, -0.18502394470995279), (42.0, -0.19486625914109013), (44.0, -0.20480983791835441), (46.0, -0.22874171292099749), (48.0, -0.23882758001427645), (50.0, -0.24778194021353439), (52.0, -0.25671366392786066), (54.0, -0.26565540994362763), (56.0, -0.27476946646436579), (58.0, -0.28463764186632368), (60.0, -0.29385220960212266), (62.0, -0.30299942625059756), (64.0, -0.31142671294544394), (66.0, -0.31898825060282698), (68.0, -0.3258381874284435), (70.0, -0.3215248160243398), (72.0, -0.32730981473683474), (74.0, -0.33168908004670883), (76.0, -0.33421827342932503), (78.0, -0.33863873488195662), (80.0, -0.34377203693685943), (82.0, -0.3507212829745337), (84.0, -0.35498014603752426), (86.0, -0.3612765383022386), (88.0, -0.36709187484624939), (90.0, -0.37452313513962932), (92.0, -0.37865695831917034), (94.0, -0.38437403004172943), (96.0, -0.39571803630909319), (98.0, -0.39151220537797132), (100.0, -0.39896797745529955)]), ([(0.0, 0.0), (2.0, 0.004744782124961348), (4.0, 0.0097977625731367861), (6.0, 0.016224811353521211), (8.0, 0.02395562319037494), (10.0, 0.032972450253279911), (12.0, 0.043046094567071209), (14.0, 0.05407224685779348), (16.0, 0.066408140272667684), (18.0, 0.079443146369275769), (20.0, 0.093639946200329435), (22.0, 0.10854191294509702), (24.0, 0.12430167622668681), (26.0, 0.14096788702791663), (28.0, 0.15822886344926657), (30.0, 0.17591663490995918), (32.0, 0.19461585787465835), (34.0, 0.21434795976819138), (36.0, 0.23394124226285096), (38.0, 0.25288718755298722), (40.0, 0.27226436526785658), (42.0, 0.29378822518980174), (44.0, 0.31632830904579051), (46.0, 0.33914748238540937), (48.0, 0.36374007933524255), (50.0, 0.39291567048297915), (52.0, 0.43186530671776963), (54.0, 0.45859746091251385), (56.0, 0.51728578393395308), (58.0, 0.55916881301266597), (60.0, 0.59964733997328157), (62.0, 0.63644319849407549), (64.0, 0.67316343131805112), (66.0, 0.7461644751255927), (68.0, 0.77179963320431666), (70.0, 0.80412631856572603), (72.0, 0.84159817738280274), (74.0, 0.87898162550951864), (76.0, 0.92122056996319457), (78.0, 0.99136746076893556), (80.0, 1.0313330840125825), (82.0, 1.0709040330392214), (84.0, 1.1258393341610331), (86.0, 1.157457221673625), (88.0, 1.1914949739916489), (90.0, 1.2245087025693409), (92.0, 1.2590220692743976), (94.0, 1.2898714254422763), (96.0, 1.3212855112508066), (98.0, 1.3545999089437455), (100.0, 1.3888761793173248)], [(0.0, 0.0), (2.0, -0.010016267402010256), (4.0, -0.019948703620405184), (6.0, -0.029821342531035695), (8.0, -0.039745341128823775), (10.0, -0.049624733297819509), (12.0, -0.059502326811754866), (14.0, -0.069389655857311272), (16.0, -0.079310204438032425), (18.0, -0.089200291021704209), (20.0, -0.099143944088897693), (22.0, -0.10909767118860236), (24.0, -0.11897054991863196), (26.0, -0.12889653132038026), (28.0, -0.13885665503760766), (30.0, -0.14875589255660659), (32.0, -0.15880674996308503), (34.0, -0.16853080481050919), (36.0, -0.17844163609997893), (38.0, -0.18816629375151134), (40.0, -0.1976980975861653), (42.0, -0.20701288968875114), (44.0, -0.21660393147665313), (46.0, -0.22647540437642916), (48.0, -0.23610873810414199), (50.0, -0.24503531519181643), (52.0, -0.25275306951386128), (54.0, -0.26178362159829788), (56.0, -0.27067021657861007), (58.0, -0.28161862165639528), (60.0, -0.29047919628600816), (62.0, -0.29943074876333642), (64.0, -0.30820980132697395), (66.0, -0.33157274514277962), (68.0, -0.34038896170499627), (70.0, -0.34806396790838789), (72.0, -0.3554131369584132), (74.0, -0.36273368532933725), (76.0, -0.370046634630259), (78.0, -0.37655690608212172), (80.0, -0.38517779250010886), (82.0, -0.39366123594728986), (84.0, -0.39266183859997594), (86.0, -0.40129689164668753), (88.0, -0.41134431191199838), (90.0, -0.41596773288275346), (92.0, -0.42468349555513563), (94.0, -0.43364292008668215), (96.0, -0.44351759677606817), (98.0, -0.45371763529120823), (100.0, -0.46263967508119175)]), ([(0.0, 0.0), (2.0, 0.004731554866228109), (4.0, 0.0094216357891686673), (6.0, 0.014216453012416762), (8.0, 0.019497706294342977), (10.0, 0.025582628803939887), (12.0, 0.032278595675286362), (14.0, 0.039648237619870068), (16.0, 0.047721625707608593), (18.0, 0.056396795893754008), (20.0, 0.065622899613262842), (22.0, 0.075404143850364397), (24.0, 0.085656506725380221), (26.0, 0.096462210285150493), (28.0, 0.10770340641610801), (30.0, 0.11964320872158793), (32.0, 0.13220503526327404), (34.0, 0.14514105878062863), (36.0, 0.15815742284895773), (38.0, 0.17192524573631834), (40.0, 0.18637816501963694), (42.0, 0.20149291745144846), (44.0, 0.21716117479879563), (46.0, 0.2325507867430337), (48.0, 0.24791235468372394), (50.0, 0.26288373835209911), (52.0, 0.27843558442659244), (54.0, 0.294516845956447), (56.0, 0.3117142378450008), (58.0, 0.32904424132331112), (60.0, 0.34669404729647257), (62.0, 0.36516520650582462), (64.0, 0.38984372923097116), (66.0, 0.41146067432412303), (68.0, 0.43376493297723495), (70.0, 0.45208208140788952), (72.0, 0.48153933859630493), (74.0, 0.50337155837651093), (76.0, 0.52009262777311571), (78.0, 0.54909802828387044), (80.0, 0.58042170009595484), (82.0, 0.61360650555834706), (84.0, 0.63513813621982707), (86.0, 0.64695535426184658), (88.0, 0.75255689948596827), (90.0, 0.79971134306514247), (92.0, 0.86801610980704047), (94.0, 0.88683234951031298), (96.0, 0.90032068400625453), (98.0, 0.91874663340148377), (100.0, 0.94211017343490866)], [(0.0, 0.0), (2.0, -0.010006926475377178), (4.0, -0.019989152514181176), (6.0, -0.029938340825470911), (8.0, -0.039829821593797929), (10.0, -0.049697495221855389), (12.0, -0.059586293949287737), (14.0, -0.06948169771812554), (16.0, -0.079453530180236542), (18.0, -0.089389896199069174), (20.0, -0.099267299588735786), (22.0, -0.10917610348399959), (24.0, -0.11911920616448748), (26.0, -0.12908779208514859), (28.0, -0.13904950400929073), (30.0, -0.14888456395512417), (32.0, -0.15893430193610886), (34.0, -0.16892498845008458), (36.0, -0.17891766282781524), (38.0, -0.18900039612994873), (40.0, -0.19915632141154962), (42.0, -0.20943349413230594), (44.0, -0.21960216990173778), (46.0, -0.22961285827159314), (48.0, -0.23971825671387037), (50.0, -0.24988207260330575), (52.0, -0.25997129505696404), (54.0, -0.26996988188116611), (56.0, -0.27996906025208734), (58.0, -0.2900419837892082), (60.0, -0.3001500349709324), (62.0, -0.31038900983535356), (64.0, -0.32182846197497239), (66.0, -0.33216618851443697), (68.0, -0.34282657283114715), (70.0, -0.35328607193718242), (72.0, -0.36433837853515549), (74.0, -0.37439410563977027), (76.0, -0.38443139636420903), (78.0, -0.39445028433896528), (80.0, -0.40454662990998785), (82.0, -0.41331497990459887), (84.0, -0.42284859046885748), (86.0, -0.43318793988333226), (88.0, -0.437677177238329), (90.0, -0.44605515744303292), (92.0, -0.45204924505631305), (94.0, -0.46234148633415162), (96.0, -0.47283799875966642), (98.0, -0.48338569803807491), (100.0, -0.4936284158357393)])]
boundaryStresses = [([(0.0, 498808.48457545997), (2.0, 507326.03167963435), (4.0, 503268.90501521452), (6.0, 512611.03825117508), (8.0, 520488.92517746356), (10.0, 521173.30658706627), (12.0, 520956.95411136386), (14.0, 522574.86977256398), (16.0, 524296.608435045), (18.0, 524013.19988861092), (20.0, 520665.08413700241), (22.0, 522840.45745512733), (24.0, 531793.84311855293), (26.0, 538096.55076055042), (28.0, 540982.29078484944), (30.0, 559486.96509520255), (32.0, 548570.9226431729), (34.0, 516252.07166485355), (36.0, 533901.14191331039), (38.0, 550187.47683754622), (40.0, 559781.25407258898), (42.0, 562876.20409591321), (44.0, 568876.88653626246), (46.0, 579169.8851129238), (48.0, 588459.66152185854), (50.0, 591632.26128093619), (52.0, 595012.82573988044), (54.0, 607972.21756583755), (56.0, 608521.35474523553), (58.0, 612508.75798097241), (60.0, 606204.87965948088), (62.0, 600016.57643427909), (64.0, 599613.72449458041), (66.0, 596803.06587951921), (68.0, 599010.56074172514), (70.0, 593158.4190857436), (72.0, 602677.89056780247), (74.0, 597342.8645610417), (76.0, 602452.526117092), (78.0, 605495.9232224205), (80.0, 603340.40134755231), (82.0, 601540.97443528078), (84.0, 602341.55993526138), (86.0, 599440.60391004407), (88.0, 599652.50398119434), (90.0, 603854.40866710828), (92.0, 603505.51853578188), (94.0, 599165.32054569258), (96.0, 604811.00769606687), (98.0, 606850.95872267138), (100.0, 602467.49832841021)], [(0.0, 249946.0878663632), (2.0, 2054463.0187024542), (4.0, 3285296.4771864526), (6.0, 4154866.7181079676), (8.0, 4790276.3199377283), (10.0, 5268837.1781259393), (12.0, 5649759.5816194834), (14.0, 5966763.6202539383), (16.0, 6208585.4949586522), (18.0, 6365610.3586197449), (20.0, 6396603.9499998484), (22.0, 6467197.3440963645), (24.0, 6591672.3915647734), (26.0, 6611050.3444364071), (28.0, 6475847.9040371049), (30.0, 6331479.631996233), (32.0, 5988371.6365769878), (34.0, 5076752.1206052816), (36.0, 5033635.9137891158), (38.0, 5001961.5925748181), (40.0, 4983545.0398761416), (42.0, 5062146.2539267978), (44.0, 5012812.7623663666), (46.0, 5038288.2810008889), (48.0, 5036506.0656870715), (50.0, 5017894.8093667524), (52.0, 4984413.4606673131), (54.0, 4937948.7048008898), (56.0, 4725284.9743284276), (58.0, 4414407.2202523528), (60.0, 4316475.7818231266), (62.0, 4206603.9438952841), (64.0, 4078992.7492845603), (66.0, 4119324.680936269), (68.0, 4091870.877251721), (70.0, 3946668.4569613156), (72.0, 3651526.695269194), (74.0, 3571283.7360250792), (76.0, 3548559.1566854753), (78.0, 3537517.5334733194), (80.0, 3515900.3777505825), (82.0, 3374084.2987867021), (84.0, 3253995.4999780064), (86.0, 3147491.1746422434), (88.0, 3098407.8920966), (90.0, 3045622.5771779856), (92.0, 2981312.9713513507), (94.0, 2857754.5730443397), (96.0, 2858215.861963802), (98.0, 2866767.3686314085), (100.0, 2800031.8628080734)]), ([(0.0, 997789.44199624448), (2.0, 1022890.280754532), (4.0, 1016232.3678047251), (6.0, 1008541.9123735182), (8.0, 1008019.4584199232), (10.0, 1018941.8539251187), (12.0, 1032353.863686583), (14.0, 1041945.4351353669), (16.0, 1045799.9030852902), (18.0, 1050394.5054159304), (20.0, 1047621.8011884254), (22.0, 1047636.846491295), (24.0, 1051773.6100597715), (26.0, 1052898.8217120192), (28.0, 1055527.9893937712), (30.0, 1064512.1812933031), (32.0, 1067451.4098328124), (34.0, 1063200.2021108179), (36.0, 1071509.5640806754), (38.0, 1077220.1386135141), (40.0, 1088642.4518271287), (42.0, 1103515.5650703891), (44.0, 1105150.863174866), (46.0, 1051267.0333521301), (48.0, 1063514.2080638062), (50.0, 1077211.575776896), (52.0, 1086609.5140650244), (54.0, 1099784.7689493618), (56.0, 1114234.0666184702), (58.0, 1123189.6314093887), (60.0, 1135337.8198302693), (62.0, 1157383.3774034746), (64.0, 1178662.8175270313), (66.0, 1187845.8133538761), (68.0, 1185434.8894735691), (70.0, 1178935.7164645831), (72.0, 1193973.4781268556), (74.0, 1202392.6822653632), (76.0, 1196814.426969856), (78.0, 1192695.5966977617), (80.0, 1198101.5388791831), (82.0, 1219026.5208846191), (84.0, 1226295.8892729671), (86.0, 1229210.9977825859), (88.0, 1240348.9229768505), (90.0, 1239535.5332784324), (92.0, 1240204.4993217262), (94.0, 1291332.2305407675), (96.0, 1417229.658613641), (98.0, 1220066.343819133), (100.0, 1235112.8230433615)], [(0.0, 500012.45100047608), (2.0, 2454923.1854466726), (4.0, 4081924.7849636944), (6.0, 5390728.7054273151), (8.0, 6447261.9661281174), (10.0, 7347564.8316888744), (12.0, 8091226.616717306), (14.0, 8714622.548376739), (16.0, 9259166.7111466378), (18.0, 9732839.9476316702), (20.0, 10133041.476140171), (22.0, 10489464.109934935), (24.0, 10809083.269136775), (26.0, 11044500.422965467), (28.0, 11313811.619665261), (30.0, 11640415.330602344), (32.0, 11736465.872089839), (34.0, 11667790.424415968), (36.0, 11556959.703651996), (38.0, 11386881.852334507), (40.0, 11170876.180663696), (42.0, 10943340.608260391), (44.0, 10970490.182061182), (46.0, 9709299.0411729235), (48.0, 9935327.6681925468), (50.0, 9966468.3682685141), (52.0, 10025957.959036857), (54.0, 10079866.183025202), (56.0, 10115806.726077633), (58.0, 10092768.270028798), (60.0, 9942694.2619693391), (62.0, 9675537.5230426323), (64.0, 9266536.6584855523), (66.0, 9043547.0848854501), (68.0, 8654066.5068807658), (70.0, 7677476.1168176439), (72.0, 7685308.4358440964), (74.0, 7598326.5924695358), (76.0, 7311120.912080205), (78.0, 7178776.4771394972), (80.0, 6914455.2085236367), (82.0, 6744053.8409838043), (84.0, 6529952.0720202681), (86.0, 6501153.0149159525), (88.0, 6332751.2079034885), (90.0, 6226980.1615846632), (92.0, 6018010.8640365163), (94.0, 6174191.6176100308), (96.0, 6799433.3649437809), (98.0, 5331889.1940601803), (100.0, 5462646.2090676213)]), ([(0.0, 1996107.7372432565), (2.0, 2030430.9487851928), (4.0, 2044901.2009641426), (6.0, 2037764.955377952), (8.0, 2033674.6896110163), (10.0, 2028915.3546739288), (12.0, 2023850.3670633021), (14.0, 2028609.5768572714), (16.0, 2031644.5901268695), (18.0, 2040556.6402641751), (20.0, 2051610.1413759538), (22.0, 2069756.9354372502), (24.0, 2081944.3219823053), (26.0, 2094508.7512310154), (28.0, 2104433.3808203936), (30.0, 2110359.5146453241), (32.0, 2118009.6922167307), (34.0, 2117714.717350286), (36.0, 2124537.368825221), (38.0, 2136845.9646423305), (40.0, 2147508.1309225289), (42.0, 2146960.6419050074), (44.0, 2150682.4099115273), (46.0, 2164745.2195007307), (48.0, 2177688.2103750021), (50.0, 2186052.0732708685), (52.0, 2178559.7556966213), (54.0, 2266867.9374286435), (56.0, 2184600.3136706478), (58.0, 2172527.6450204877), (60.0, 2164192.2475280142), (62.0, 2158977.2657291624), (64.0, 2155451.9635314946), (66.0, 2130256.4365509162), (68.0, 2138856.7107081744), (70.0, 2140174.7431896008), (72.0, 2141760.1747651226), (74.0, 2145308.03027737), (76.0, 2141664.4887076304), (78.0, 2144677.8664176939), (80.0, 2139060.5477818311), (82.0, 2180092.9225142123), (84.0, 2165300.5833609649), (86.0, 2200102.474397514), (88.0, 2197554.7288131043), (90.0, 2181435.425129612), (92.0, 2186268.982445389), (94.0, 2187252.0649115345), (96.0, 2190094.6498096497), (98.0, 2191044.6964017423), (100.0, 2187359.3243486783)], [(0.0, 1000969.9734900271), (2.0, 2984288.2934165397), (4.0, 4905452.6387655158), (6.0, 6605691.294381611), (8.0, 8120729.4576187711), (10.0, 9468503.538350815), (12.0, 10678237.877250101), (14.0, 11760969.44019706), (16.0, 12733779.010756854), (18.0, 13630945.779113254), (20.0, 14431407.034385171), (22.0, 15166743.188392352), (24.0, 15813199.014599694), (26.0, 16405282.561446236), (28.0, 16954153.120682638), (30.0, 17455087.316529788), (32.0, 17913241.04108147), (34.0, 18295783.793533232), (36.0, 18761519.514455725), (38.0, 19261618.192421824), (40.0, 19740298.309703674), (42.0, 20052647.104307134), (44.0, 20350230.370606691), (46.0, 20743695.082213953), (48.0, 21043011.42182669), (50.0, 21201777.852016464), (52.0, 20949109.300574459), (54.0, 21290881.560188085), (56.0, 20339772.913184389), (58.0, 20199957.597235765), (60.0, 20062397.45404581), (62.0, 20011809.426786203), (64.0, 19901390.211962331), (66.0, 18292080.871715557), (68.0, 18699349.213332742), (70.0, 18776524.5462039), (72.0, 18611575.393606029), (74.0, 18363414.141121656), (76.0, 17959489.843896937), (78.0, 15716412.334553966), (80.0, 15362282.478184294), (82.0, 14913736.336725902), (84.0, 13668868.503085501), (86.0, 13475306.400930632), (88.0, 13385677.334152615), (90.0, 13025877.668645293), (92.0, 12826576.168993773), (94.0, 12782141.384237645), (96.0, 12720191.795797801), (98.0, 12067210.751378939), (100.0, 11908647.676610082)]), ([(0.0, 3995108.6907140845), (2.0, 4032465.2648572624), (4.0, 4070560.4490105612), (6.0, 4089495.0300791683), (8.0, 4093360.3778952518), (10.0, 4090681.2019325425), (12.0, 4091765.1474766429), (14.0, 4090443.3256854131), (16.0, 4092068.8316445369), (18.0, 4093517.8091291254), (20.0, 4096708.7002796447), (22.0, 4093856.5684778537), (24.0, 4099026.9721356751), (26.0, 4103782.8025982953), (28.0, 4114615.8204437955), (30.0, 4115388.3491369863), (32.0, 4125318.6118878596), (34.0, 4136318.0967657357), (36.0, 4154088.9507381837), (38.0, 4168560.5756045487), (40.0, 4190683.6475337865), (42.0, 4222679.0546678323), (44.0, 4217582.7536232313), (46.0, 4231413.7131091906), (48.0, 4245328.1637506792), (50.0, 4262317.596761792), (52.0, 4276862.6891374663), (54.0, 4299630.9529904397), (56.0, 4317936.5735383797), (58.0, 4332143.8261937704), (60.0, 4340710.5160652157), (62.0, 4351704.6181044076), (64.0, 4331899.0499890437), (66.0, 4346560.6004851665), (68.0, 4350309.151357621), (70.0, 4451465.0041349996), (72.0, 4368150.4905709065), (74.0, 4355123.288838651), (76.0, 4437784.5514870286), (78.0, 4357770.9201685479), (80.0, 4339732.6290941378), (82.0, 4359937.0816996535), (84.0, 4489347.49488331), (86.0, 4676329.253573684), (88.0, 4260903.2248005113), (90.0, 4240574.454691139), (92.0, 4232213.1303704092), (94.0, 4391286.072904394), (96.0, 4517177.6969841179), (98.0, 4621378.5745354295), (100.0, 4708908.5325270519)], [(0.0, 2002327.3615885368), (2.0, 3973177.7214580504), (4.0, 5973160.6801918671), (6.0, 7939137.9016189827), (8.0, 9805734.8749265578), (10.0, 11547280.43613776), (12.0, 13188294.031427523), (14.0, 14734735.166436888), (16.0, 16179631.816730134), (18.0, 17554285.819254614), (20.0, 18844746.687188078), (22.0, 20062819.926498376), (24.0, 21207333.175536066), (26.0, 22280927.355785578), (28.0, 23304416.910955295), (30.0, 24234500.407486245), (32.0, 25152482.516240321), (34.0, 26011386.210209385), (36.0, 26849140.617919192), (38.0, 27601049.600656692), (40.0, 28320400.682762962), (42.0, 28929576.559461221), (44.0, 29554574.584265098), (46.0, 30160535.768764962), (48.0, 30822298.088163897), (50.0, 31559945.412474211), (52.0, 32269863.320968095), (54.0, 32963973.700301539), (56.0, 33596454.964473464), (58.0, 34235734.215657711), (60.0, 34853580.02588921), (62.0, 35429765.53179808), (64.0, 35596467.289592519), (66.0, 35900591.38195926), (68.0, 36217539.098046221), (70.0, 36775404.831859805), (72.0, 36554146.948753588), (74.0, 36741647.477552824), (76.0, 37373237.059597597), (78.0, 37137839.519618347), (80.0, 36626061.161271989), (82.0, 36471091.084997803), (84.0, 36963889.184066005), (86.0, 38061988.943650372), (88.0, 33397023.554363504), (90.0, 32677364.432841744), (92.0, 30695148.401372842), (94.0, 31004641.62340536), (96.0, 31842251.432702154), (98.0, 32354081.819735326), (100.0, 32519369.717549808)])]
relevantMeasurements = ['S22']

try:
    from abaqusConstants import *
        
    elementType = CPE4R
    elementShape = QUAD
    meshSize = 10

    instanceName = 'BLOCK-1'

    boundaries = {'Bottom': (10/2, 0.0, 0.0), 'Top':(10/2, 10, 0.0), 'Left':(0.0, 10/2, 0.0), 'Right':(10, 10/2, 0.0)}

    # steps = ('Initial', 'Step-1', 'Step-2')
    v = 0.005
    vNames = (('Bottom', ), ('Top', ), ('Left', ), ('Right', ))
    velocityTable = ((0, -1), (100, -1))

    largeDef=OFF
except ImportError: pass