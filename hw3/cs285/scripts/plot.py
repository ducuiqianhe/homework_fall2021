import numpy as np
import matplotlib.pyplot as plt


x = [1, 2]



# 500000
# 1.2
# [-216.6134496574656, -166.1437457862082, -155.2851035842549, -144.76134468539829, -134.3481713192592, -125.07510302234526, -89.80549072310455, -61.751682006904524, -33.824444852211066, -5.150844675146383, 25.976124640288194, 49.81
# 636838252156, 48.23238366874761, 49.39907137304123, 54.58164457460843, 66.77650702495808, 75.71207352586002, 94.5555881905778, 103.69793593951056, 102.20129389578928, 103.79639556297862, 102.25851006323495, 96.79894263894879, 97.344880
# 9441826, 95.26777827279649, 90.97787490433066, 78.91936734173107, 67.46433076760341, 33.17844098786013, 30.418823080074702, 34.59470230531571, 44.35646203920376, 68.71046682238925, 63.135529868935016, 69.27543067550461, 60.276063036814
# 946, 27.423477779563896, 19.452867817345446, -10.936409489699724, -24.27124608093958, -46.586331155467775, -36.42888166720486, -4.805793482520067, 37.96431826756157, 69.7753799348241, 83.21815838739595, 85.96595063454626, 109.657096489
# 1522, 107.19211742856723]
# 2.1
# [-233.99722777772783, -206.1931894022531, -186.83859375664383, -163.81624916930397, -150.97124556427488, -134.27077767432192, -114.7031318276439, -105.14229291495886, -89.15709423562838, -81.28470330032657, -66.8052767326088, -42.
# 02112716154089, -20.576533711087272, -17.68343814623839, -2.5663551342852706, 4.330061356687667, 15.992460294329803, 21.745880800703954, 36.31666723594565, 44.55901568211496, 53.561723610658284, 70.06004558561912, 72.40929555621531, 71
# .22898296091132, 77.96639364900189, 79.2916945912272, 65.54486279533812, 65.83854565585312, 52.62519980235253, 40.58915064093412, 26.603684106398564, 18.03824920119831, 9.627743761401025, 2.7096316794368995, 1.4268658617530425, 2.17957
# 4567606623, 5.51875122079138, 23.087813928463223, 67.37557458187811, 110.75161765855177, 140.72816212266042, 146.722377513751, 152.36863154983237, 156.18557997500216, 155.56167100772504, 145.4684408472067, 122.43965936942011, 95.758509
# 1281756, 100.52018721279514]
# 2.2
# [-256.0353636428788, -182.12187833552088, -162.24835639726234, -151.47754893334323, -136.50532991170195, -101.34129247041227, -85.11498021186121, -53.64373260970213, -40.828049610464284, -47.40151988572134, -32.36368846838228, -13
# .53238716549313, -3.0844536415758865, 10.21642752894399, 20.703544138638662, 38.81073981230129, 51.88329293178428, 59.94298875300578, 62.81956521654378, 61.0706515530801, 59.154467134337445, 62.29089535688912, 55.73008803646056, 49.574
# 01638133582, 28.95922752396567, 25.89450149764506, 35.79589102779326, 44.631070403144406, 43.32337333144469, 46.06976203323668, 37.93679732666823, 34.43541713237367, 30.75473661316999, 32.35919438055278, 36.317877803815534, 69.00912105
# 488689, 93.03880525077993, 96.91266320415701, 92.22858392319293, 68.37698840531048, 35.07879832023562, 8.349391640456977, 32.33405453684581, 69.36590665196572, 57.644833386838684, 54.5749498059051, 44.51244812205962, 49.78886663580672,
#  -9.69653623093441]
# 2.3
# [-238.5213947563621, -190.88956446529662, -170.63761506614995, -152.4351674756052, -137.51003258891168, -128.98336332769733, -114.29493749784201, -91.28938025793765, -83.63445027033927, -60.99996635989971, -35.08041904380622, -12.
# 19367093838165, 2.0505474369747985, 33.738628155186255, 59.84454228283802, 85.51794596188591, 87.11007423694707, 87.18570451597998, 78.01064700126459, 77.38333983939364, 62.419838605292014, 52.34756172398379, 38.9853778970412, 54.21022
# 4424325105, 50.98350212289341, 60.933582970211646, 82.35675345536079, 89.5478991956936, 102.19777110704334, 107.22203792175647, 113.18570075298929, 126.99991190469179, 116.3602995609704, 124.78591943049287, 124.49798295544905, 122.4215
# 0584891138, 121.20378760684429, 103.31243254109508, 114.34389561517554, 115.77969173349766, 99.41658225191215, 77.67915932398826, 38.155470826422395, 38.8638517109222, 24.862303598902134, 68.34716984429662, 82.22455235516827, 26.937089
# 150889978, 73.87068242036261]
# 2.4
# [-218.92911842148962, -177.3459309013078, -154.39349789851346, -145.4308742916803, -138.1921316635052, -129.15823155977606, -116.43655889997164, -108.38188943854969, -112.88248446614563, -98.19258632795169, -90.78659777590748, -73
# .93437335329276, -55.94019467631935, -34.84505475713424, -17.137482127078943, -0.03030717085240539, 25.934655708138806, 35.93397045891682, 50.004762941642255, 60.851504148154596, 71.54340526140331, 81.21857743509753, 87.84104795022205,
#  94.25621517086194, 79.5122983890806, 67.63233168305914, 38.87553172261784, 44.61576066685504, 59.46347482009778, 83.46097583143053, 66.89431663256259, 33.70584695430106, 10.81780003033728, 24.690949322091356, -7.572288231248321, -18.1
# 43259714264502, -20.241688943108908, -5.06677140472664, -11.384222098503477, 13.031294583971155, 41.67081210118545, 45.226671113220256, 63.453700172695505, 48.042649476607984, 42.36725457984712, 55.39857867387602, 63.33884583173699, 84
# .38708532353452, 71.27512966729002]
# 2.5
# [-227.02919180936175, -166.66063877664445, -148.4280552726167, -132.0823498756927, -124.32129437525742, -121.95599884611674, -107.7688970985725, -115.1813381972058, -120.47645668646653, -111.9742760134457, -99.52193629406615, -78.
# 80500704671813, -47.35541004625039, -13.853742560841335, 9.6657202260075, 29.610262503369086, 43.06185735460328, 54.689754754579006, 52.298855166094285, 50.2878678228312, 54.13392416037666, 70.54087167576323, 77.01918468716396, 70.3798
# 318021858, 73.022159178527, 57.131986367512575, 40.908651888689775, 31.176781189527038, 29.08330620741999, 36.00192279096562, 61.63582704477553, 59.80078737043461, 63.5012234363895, 85.55403433987169, 101.75476808362465, 104.9228435363
# 3036, 102.45347008495094, 130.26966498782917, 139.52889930080374, 139.84900414604607, 152.50602773464345, 155.89436084031362, 163.92609382331815, 152.3531496555189, 162.0100768617871, 174.51017475892178, 153.49771641834263, 148.2848333
# 353286, 110.60249602337872]
#
# 2.6
# [-250.9446046116326, -174.3063933212322, -150.66242636322409, -131.52867120555482, -123.42224637243896, -101.58394314295946, -91.88734714773459, -84.60002461797342, -86.24497237794122, -76.72588193316568, -44.50256032320735, -25.4
# 76968623555226, 6.302335676721859, 21.94009521531424, 33.31846844216421, 31.654424560798578, 35.83615253597484, 40.33161755692602, 45.5017383368303, 55.07959570197327, 59.21152762582661, 58.3616178672281, 66.08869001975108, 80.19178589
# 704644, 75.38334217414462, 75.62703246475738, 74.71104676706942, 73.86749847991703, 70.31943127110189, 85.04650762621333, 92.7805418070403, 104.76674564813163, 110.5846915703953, 112.31609026810476, 126.63291566667483, 140.573423046595
# , 128.47917216676697, 115.4166077842173, 99.13981130202527, 114.21488503940073, 115.54116204284165, 96.55856336662553, 83.44760405543832, 97.61962804497009, 77.03333304502729, 45.12352130609268, 65.08463920883493, 51.87338150947377, 10
# .171786851109028]
#
# 3.16
# [-262.7539681235195, -256.2212562304353, -277.84435676920435, -282.7611654686831, -278.1599122549681, -284.27511766227644, -266.7907692346903, -255.48752640827007, -253.16042689128727, -244.63762583230996, -238.07047025190036, -23
# 6.76415222209695, -231.6235803532799, -226.38823868357207, -218.5536045443823, -215.37944550175962, -208.56594726094147, -207.10254778946634, -204.78151494133573, -198.60653129467804, -198.81159285258389, -197.48518541336173, -194.3724
# 5879601562, -190.37442228797028, -188.63745790496966, -185.3714015341601, -184.56217693225076, -183.31142346170063, -181.4615475308253, -179.24068621817264, -177.09223962992294, -177.0370141495867, -175.97861528806868, -175.39145766171
# 205, -174.24637088606806, -171.7443498228791, -170.23279880190603, -168.98761012275656, -169.3816291631773, -168.41090034837103, -164.18031134346805, -163.07545061818612, -157.3358917251387, -156.2670304627629, -153.3229825453806, -148
# .74231659258376, -148.4845167809687, -146.58595629248885, -144.10118425197422, -143.71203324130045, -141.47717428669387, -140.04838205386102, -138.369611200048, -134.76846872825084, -133.65569919636636, -130.1845445419583, -128.0003600
# 9965962, -128.3416448011432, -119.48599101214937, -116.09401368052255, -115.12143650888356, -113.01199228140025, -112.93714378857202, -111.68560902583708, -108.98019138924252, -104.80506140391282, -104.07831679691421, -99.4219815773124
# 7, -100.3723047793243, -100.13756259468133, -96.32839026552757, -91.25670289451938, -89.24264035112509, -88.5834219752508, -87.81299744207217, -87.21548335221432, -86.02495993647713, -84.27513708146552, -84.42891279153606, -80.11865949
# 469687, -80.46654830752304, -80.98381794241979, -74.15176715572588, -74.24158234425084, -71.76481248974014, -70.7917590273822, -68.33380395841384, -69.1813029459729, -73.37131750801285, -73.2836172315233, -73.23982361970276, -73.532769
# 04136365, -76.43552289893512, -76.85833132688806, -77.26866470947849, -77.57302479772864, -73.38337802535457, -72.67366199250242, -72.87369273911813, -72.2291680388293, -71.66673510856464, -73.8223639880928, -72.21807175582336, -69.680
# 00615339659, -70.12342866897167, -67.50025233681626, -65.40175006309023, -64.08088581226276, -63.87525453537198, -61.2914041171639, -55.398500701836355, -55.12751224879679, -55.45617263147704, -55.50518796082662, -53.39086074157233, -5
# 3.43589974595004, -50.6791283754265, -48.51277218276764, -45.29982593925545, -40.22657315331423, -39.92024247042152, -39.31907051255879, -36.21650467037648, -36.273866294326325, -37.96970945334563, -35.81960252058613, -33.6941047415169
# 95, -32.67720210340879, -35.249658113288994, -34.3010371027519, -30.342496987418716, -32.163157390733716, -28.178862569095614, -27.550835866829335, -23.18991502934325, -23.092386233780836, -20.114883403010303, -17.3662521742733, -18.70
# 9359884129995, -16.28756074829934, -12.625878405122867, -10.769556577425105, -9.408843233565987, -6.644224391554244, -3.478905915693923, -0.312171754900869, 1.6953390727813558, 2.8052993731343956, 3.7436125588411118, 10.23000968722238,
#  14.64240158398139, 18.694282336316604, 26.542093378125998, 32.810569806383796, 33.85743245872926, 31.88040226871476, 36.51595456203598, 40.33362314139043, 43.75108860651612, 42.92228624863553, 43.32304044646319, 45.867450157499555, 44
# .31444418204058, 43.218561395653325, 42.66921245823142, 43.644213558112234, 49.82413109848897, 52.882273036461086, 58.00573172977494, 61.64667700575754, 60.95870390095381, 64.16313833399764, 66.9460869497886, 71.30187021754782, 73.1836
# 7359618632, 76.75333390808471, 79.49353776589238, 83.06648262032282, 85.34509242153554, 83.34257471666655, 87.49430494128657, 89.605404701003, 89.5513017478512, 90.13030123638299, 91.11454707955772, 94.10002787066638, 94.17238198287212
# , 96.11823604950085, 97.37976405775876, 104.218030517508, 103.09263092640467, 104.98716804052945, 102.57452311765991, 96.24745213926268, 95.8244155285775, 96.95265436448693, 96.72990032417954, 99.30010213967296, 106.81499473431415, 107
# .45116966011147, 106.82995081887037, 101.91552892892163, 101.59273210897283, 101.68342812219065, 98.97750572632305, 95.35067219884567, 87.94256671547971, 82.51593893758982, 82.10304268113602, 75.86685285820407, 74.52380687437993, 65.34
# 441050485799, 59.531044798964764, 58.711706518430326, 56.23026289677668, 58.96272455008373, 56.5836193481713, 49.19683815576706, 49.13779345217908, 46.783478384895034, 43.4850481597101, 35.4274153414024, 33.204007710166955, 27.08348317
# 311641, 32.719757782224036, 31.013308323361272, 31.372967380560173, 25.247021126070248, 20.70169765785222, 16.15267839097751, 13.532665326892268, 13.836993846037803, 17.546207088041616, 22.383679787637988, 27.84206233413436, 23.7696938
# 07541984, 31.168294671585276, 30.36934999501469, 30.65481929586921, 35.0058957578186, 34.23299116015769, 39.96456197244211, 44.70940169036174, 43.848823013828714, 45.82284867327936, 46.49131461712369, 50.49971493049657, 49.787425638356
# 666, 51.38044491024436, 51.97698199915924, 55.261775379514646, 60.20164030819592, 62.87175720748058, 70.28949203840165, 75.58242267595429, 74.56233548670915, 72.76893409859211, 74.93194033211813, 78.85142780019218, 81.56335736239035, 8
# 3.58080391943254, 84.44388007319355, 86.27719529494009, 81.67778549148646, 76.7231959520786, 80.35205721195243, 82.42706428633585, 83.21708889271355, 85.9535911172092, 92.23129317687776, 95.56535849104493, 95.48449887845283, 94.3903323
# 3845755, 91.26410402974305, 92.45595801351499, 96.76371581276537, 95.94214516600579, 96.94291037547576, 98.67957588853153, 96.42011387949172, 96.08556998913126, 96.91850842348964, 94.32269973642184, 89.02456537871774, 90.84353676257075
# , 86.28194417399935, 83.01605414852276, 81.35603348604394, 81.05279568569539, 77.73838500987792, 81.7526249539549, 83.8845829139542, 86.11693125562905, 91.55405739071435, 97.20177172743634, 92.53987077552087, 98.66886962971607, 95.0076
# 6542089079, 96.10315554693307, 93.3588573056104, 91.00050374353455, 89.65608779499826, 89.32801349950876, 91.21463572812196, 91.12635606883677, 91.05686898648113, 90.64900879080231, 93.61263989196435, 95.07295788533132, 94.652647751419
# 27, 93.89619657426863, 96.657394697725, 99.8374971580999, 98.28419654091047, 98.38105483824447, 106.13056856043858, 111.17414147063101, 113.12359696070243, 118.58554726986408, 116.61208116865568, 116.09050493957888, 113.20812358919427,
#  110.74253197628583, 111.1855710495327, 108.6222570398419, 105.53691356753833, 107.11380799191085, 106.82363178601612, 108.2763008053853, 112.03321707454117, 109.15038560915285, 107.17623417340336, 104.79578838442339, 108.5891476315865
# 3, 112.64561118900718, 111.65543970184086, 113.07334133615133, 110.95756875258756, 110.6803673461384, 107.17364446041672, 106.48898499896478, 110.31411394870287, 106.6953166451471, 108.1889048168133, 111.25284554430871, 105.13544301943
# 598, 104.75991020553506, 100.56624519981091, 99.16899535218336, 94.0879579698647, 97.74408069263076, 96.53831381931992, 94.8816190320045, 94.07567785534248, 101.00743700167523, 99.33414529333854, 101.6806899734924, 96.88741338878846, 9
# 5.22295233318789, 96.71415100099338, 97.59109194413583, 101.15474637958471, 106.33776625500803, 107.71911046113473, 114.98519061838255, 112.54034535650482, 110.69018769812608, 110.43162208091638, 113.98440200926589, 119.35306707791831,
#  119.51456529053938, 123.43355614835095, 122.66801414254034, 123.27363366186921, 123.01632248434946, 124.85703569903211, 124.1336961610653, 127.58031193382467, 133.75176811982823, 131.85820954517186, 132.83737878852386, 134.74651184831
# 194, 133.9317717751146, 133.13292867377106, 132.07458326440374, 142.86746011130862, 144.96535332957063, 150.21800452521623, 150.97935572732487, 153.8223500375806, 156.76143851458085, 157.9110450216137, 159.26915658809537, 161.013710021
# 36813, 164.57137102698408, 166.48331182765403, 166.31301927363677, 165.27124700171538, 164.96522508084058, 167.34341042931763, 161.91202891617095, 155.03210558516437, 152.72081158537668, 142.85781425673431, 142.05091281644152, 140.5678
# 377106428, 141.7830111980258, 143.95668823758297, 142.60797172713035, 144.0624916372175, 136.52426352203457, 134.01477932637354, 135.90689834885333, 131.04298748699182, 135.72487523994886, 136.17507494648768, 122.47213472287082, 129.90
# 69482577982, 137.29280651960036, 141.68555311501578, 140.65897214714414, 146.77504405261084, 146.26513523917413, 146.38820243814598, 139.29551393398478, 135.35484056880395, 132.67542568233608, 138.00171068766784, 135.9784075531838, 126
# .52982713809322, 112.54180804163234, 104.14136384739328, 105.87436243712949, 101.49033947553323, 96.2322859263323, 86.14079059115984, 83.18794961783516, 69.00220773931487, 59.38621335782237, 46.85540097761851, 40.15453981830608, 33.021
# 95459071253, 30.16184827741613, 28.281884265749504, 32.12410630178215, 39.36913692645814, 47.901178508636676, 46.356022721617585, 24.652915715641438, 24.84878720647297, 31.488208858398963, 26.687261387935642, 31.73843895688599, 37.4645
# 0879118263, 36.65197906092961, 22.383673827434855, 16.462993759514582, 9.420723092231107, 5.267182922783987, 4.092041901038023, -6.452994778731745, -11.190356506153002, -11.947830708714246, -21.055040838076962, -22.355991819461615, -16
# .846704320788884, -14.46667444362745, -27.36301019846238, -29.94776893870803, -35.495690492423776, -38.48449997073482, -42.34097900359027, -33.83522609184214, -27.578400064919006, -17.593668671779696, -30.357479759740905, -35.055970199
# 136, -49.28598529789033, -51.00614777451068, -60.78380173482898, -62.77168392700913, -63.444849701931815, -66.20250982032539, -71.15692665305605, -76.96320643272028, -78.92101469648814, -86.44457661515264, -88.35644451750655, -94.45808
# 541690809, -86.9696775188263, -85.78934062465011, -87.81360094593907, -93.19067488757213, -98.4476817331776, -97.57073938845315, -91.58976360651766, -78.97586260962139, -79.50195488318914, -80.993134304351]
#
# 3.64
# [-262.7539681235195, -269.2346434315623, -268.48164049067236, -265.665745296706, -252.7481494575189, -241.22464427126656, -236.12823800485273, -229.34697562271634, -215.63904717991457, -213.75747438478012, -216.9967513248392, -215
# .5898505228519, -215.08539287559222, -209.24948334766387, -207.28135183770956, -206.05758068226035, -195.28378831878294, -187.26214067632162, -186.11348064173868, -183.2289311149735, -182.28217495240776, -179.31999883897433, -179.10163
# 082176487, -177.61643190354226, -174.97100685042085, -166.92486229004308, -165.72401536749413, -167.0389267958505, -163.3277042992112, -160.83968484615372, -159.98808184863094, -159.0846808569343, -160.09535141257763, -156.786585433654
# 04, -154.76054073560854, -153.5423590217496, -150.52817403303925, -148.8116112535107, -148.8791860048651, -147.75988720786975, -146.79521728409762, -142.52641021311288, -140.53594397188562, -139.94900980203718, -138.64508744524065, -13
# 9.02043875002778, -141.28455648679574, -140.47535828210187, -136.96262334922199, -134.69830263596137, -136.57929452235058, -136.23858783563193, -131.75913919063072, -129.18761474043052, -127.65992932897427, -128.393412492266, -126.9975
# 7005462588, -125.51460795500991, -124.99657665305463, -124.63970972830607, -119.37517527359772, -115.88319557317925, -109.68700906765045, -109.14464119831952, -108.46417444200533, -107.29914460623566, -103.97723337433746, -106.02527376
# 616497, -105.43749756071877, -103.43421322621649, -103.8119821762922, -100.29641949880279, -97.76932159256128, -97.205204516179, -97.54926996744321, -95.23793297387093, -93.15239184563941, -85.2510077335445, -84.02694491385382, -82.365
# 1362247322, -81.23652252575266, -83.70961207629261, -82.75368740583298, -77.69441004351386, -76.69818792736751, -77.04428046828657, -75.18002685359002, -74.17262025256441, -71.92179384980322, -76.14222419306105, -78.63760266442823, -78
# .93083844792996, -71.07252344498822, -73.85858835707766, -73.92956026809642, -69.78691327839242, -69.87969665458729, -64.48667079146631, -66.78116341683001, -65.21479816880557, -64.56408421728746, -62.26430250196053, -62.3253688949454,
#  -61.52000922432519, -59.475543354178306, -59.831488376696576, -54.37209779755914, -52.594526321053664, -49.22340753385333, -45.131262860907455, -44.53532246246681, -44.50993167198277, -39.61805087246173, -39.427185939218916, -38.70641
# 933782126, -35.20046028223012, -30.060896239266018, -27.773652346370508, -27.232121453771924, -16.602135186821833, -15.611068115138337, -10.960040160391749, -8.374612234345475, -10.245882335827208, -11.582937304411864, -11.155758632650
# 103, -7.032729086478281, -4.804158519175826, -2.0914112690966173, 2.7905232178526806, 3.7298235059486604, 3.262724077744015, 3.2341024392093267, 7.122040226424438, 10.341148812841164, 7.983702761129023, 8.431435409820686, 18.4716143910
# 02486, 22.36845260018104, 23.26061346391269, 25.586386075391573, 31.262752526642917, 31.838880910134176, 33.64364080958489, 35.987454408022856, 35.703094082599115, 36.377091496860466, 36.99161707961963, 43.553439878331545, 47.625795093
# 02507, 46.99353003952878, 45.14878234888076, 46.38374907114966, 55.35412526601658, 60.66276268466784, 58.820974432422716, 58.644971008698896, 64.87757927223595, 67.39050696836017, 70.4606575983407, 71.65431636948033, 73.6004522431343,
# 76.88493810262807, 77.23639832387047, 81.389147545411, 90.19802621393401, 88.9228405591782, 90.31846035643963, 88.10050381701974, 88.73570778426081, 86.01524341129421, 84.18713020853076, 85.60990606168546, 82.18958798294108, 81.7768384
# 6320915, 83.23769544406022, 81.73047429268846, 79.40566687171867, 79.24998966959676, 82.02540755443358, 82.34054273512238, 85.79306969801674, 87.21073075729231, 86.94529279500068, 87.3832492588966, 83.85739669638315, 82.93959278053615,
#  85.00025429025912, 87.1951654807538, 90.93188066192239, 93.10854082009186, 90.48142218746607, 88.18450771372319, 87.04318627956725, 86.9016938850648, 86.11897882876208, 84.88585380092827, 83.10066592740564, 82.88240160780569, 82.52434
# 676485039, 85.53872302156233, 85.50639173286137, 82.9853154968036, 82.56954252156487, 83.22087943000959, 79.70118457277654, 83.0155079151083, 79.95287057264085, 79.09220655748281, 81.37407168240321, 83.64553582253698, 85.70323097979644
# , 86.25778986911162, 90.9717006516781, 97.1465804985622, 96.66479473545172, 95.70159926130744, 96.95418392460799, 98.45454884561528, 101.18885913839512, 97.95914243757151, 102.23173301650462, 100.81357044464089, 99.00380146750018, 101.
# 09019593990844, 99.1187500206625, 98.78505917728991, 101.40607064317969, 102.29600899528228, 103.92220653692883, 103.3290792751905, 105.35458283180775, 108.94196342065514, 108.1884769841008, 108.23037594518318, 107.71259418450707, 108.
# 63085994018473, 110.30757571634719, 110.84987227891355, 111.05174772782075, 115.25879243860659, 119.40768961118945, 119.45097564211511, 120.41774388053801, 121.70025965024124, 118.28035998448365, 118.88630935823944, 122.9581468636787,
# 121.21716421858522, 122.3235757516809, 125.10026948613569, 127.27323998195628, 128.4723126263129, 128.29808189356936, 126.30661600868339, 127.01285124139321, 132.81227310578947, 135.7645118341603, 135.59063035744012, 133.47374574709372
# , 133.1787926294314, 133.98442758884036, 133.321786399374, 132.5757593952302, 131.31926225594748, 132.43759023168147, 129.55805218548997, 128.29945927742696, 127.59825846002902, 130.27649262127866, 128.06089904490693, 131.363979850888,
#  133.65333223997212, 134.64547341122827, 134.2265619344973, 133.41888455506518, 133.94210392193352, 133.2685735854503, 132.448014395023, 132.0965285462465, 130.29108578541639, 141.35879367068958, 134.85522398318665, 136.2850109210576,
# 137.14287734793675, 135.30830405845586, 131.8705650669546, 133.95608925563613, 131.71130178515588, 131.296362607475, 134.36991164206125, 132.89883762390846, 131.65786860356923, 133.14307448625993, 133.83377129130233, 135.15647539783552
# , 137.19924896687982, 138.86302344421202, 140.4865907788261, 143.3304878032572, 140.10633869418888, 140.99617447457243, 138.18196677305016, 136.75080221068941, 136.30727279893156, 136.9085560857897, 135.41127174882752, 133.854107817957
# 87, 134.20852738082738, 131.5021546153842, 137.3809607612448, 133.00502000448603, 134.3083725300543, 134.9367709297223, 130.75876708780055, 127.4905404575901, 125.55178250407593, 122.82877847396259, 117.4841407031527, 114.4380068600819
# 6, 111.6703472376695, 104.07467831796295, 104.67552802846929, 96.11951978758148, 89.25408491929399, 87.22625086092526, 89.34772306348293, 88.16757828919805, 90.81508437908437, 83.9476677913706, 83.89977496791458, 84.29545138998603, 76.
# 76093576269767, 66.58877559566515, 69.02881177209628, 59.031632018192106, 46.73860128440943, 41.28131141381949, 31.627940567960913, 25.471564416547757, 33.064617141768935, 39.86439456281248, 22.303667731054993, 23.200969872424583, 18.0
# 230908669609, 18.436698499643484, 11.462473873689149, 3.7620404219305392, 11.859796404597692, 12.433916725448936, 17.68892382579787, 28.5341490523196, 32.876798184017886, 36.276770355423444, 39.98427313023672, 47.27100789732873, 51.157
# 357169864596, 56.107532317676586, 65.97598701892598, 65.7149948112705, 65.3668017775968, 61.6694799503373, 71.15782592318436, 69.56447793714108, 64.50413408264014, 63.06463147229593, 62.07865199136739, 52.68467160099063, 57.73652130757
# 412, 59.003010576662945, 59.47894872334864, 56.46450266472676, 54.73965166797736, 51.09887699620704, 58.17714121723074, 63.32933932421793, 71.07170444829224, 71.45823848577533, 83.58934225101808, 87.03833489133109, 91.30242784445579, 9
# 0.11001072928273, 91.75269091574236, 94.74500790860209, 99.78848728500103, 100.33976378874212, 79.79049119160095, 83.75278054652145, 78.50573021073495, 79.56811345324923, 82.92800915999572, 80.3501190209126, 73.49636978252789, 67.87265
# 039268534, 67.62288185585396, 70.38642978942715, 65.66832997636256, 75.18518846832698, 76.6397683740314, 72.45719839381972, 69.85010713667036, 82.29499654710833, 73.9218471836227, 77.64467497105221, 75.42319302834973, 74.81663336256152
# , 80.73184545454829, 86.21847884783216, 80.62465863792154, 82.97733668015513, 83.64309657605641, 82.25456258146156, 74.07781421906473, 75.56080641097682, 75.57349534950534, 77.73173601552966, 85.17375491953231, 82.21216454846275, 83.70
# 095106146259, 90.17020132455318, 82.96393078066272, 82.39565031446384, 80.3046731663692, 92.77277878940203, 83.36472041583873, 83.49194215856838, 91.98814355412387, 92.90439332306543, 97.65103534353551, 83.08708157330808, 80.5253932158
# 7865, 80.46766215493201, 73.26872096213498, 79.36726212153768, 78.14461355106772, 72.90622101556956, 71.295597738373, 78.87639776731419, 74.87168594540123, 74.08976407604673, 67.03548415697051, 68.84724213599645, 62.091311621422825, 65
# .200558870944, 67.10461451623569, 59.54890400299658, 50.74443188540253, 56.97000766472258, 47.76115346784624, 44.323691969973794, 30.889506234100377, 33.29239822923297, 29.647692853723726, 24.20850223251374, 21.6234816926029, 20.795574
# 85063305, 15.522356856544416, 14.183074939375667, 18.911971761339792, 18.381144865008505, 26.274661303472683, 18.835287573795075, 18.414609641597586, 26.576340252553923, 18.269126276601092, 14.089769021361779, 17.666263592863505, 18.80
# 512110816099, 13.818213433789811, 1.4161046274736762, 2.565431005383059, -7.329960883805897, -14.953808703533824, -15.324426709674551, -17.21317894899051, -25.187124876766383, -30.23102461885009, -33.74519768927499, -44.438351533502534
# , -50.49207272729496, -44.14240154681462, -55.145673822206184, -65.70833019418153, -73.70256963468516, -74.70416627304552, -78.14641773767043, -74.92933126655775, -80.35432122561423, -89.5142142957433, -85.1912585869846, -87.8426425307
# 1883, -94.98759090150912, -96.66729262468976, -100.33366063452624, -117.69293633775628, -125.0140616529354, -134.67246902419, -138.0334514054054, -130.45082695714981]
#
#
# 3.128
# [-262.7539681235195, -267.4564923022648, -287.08762843835706, -268.5370149609911, -270.66742804675386, -257.1354743998491, -236.57576389317367, -234.5284336780565, -236.30808673642363, -224.34947600735987, -218.79120218713985, -21
# 9.75527457674988, -214.8574790287251, -205.60241729214903, -204.72326284934607, -199.21034281162855, -194.99774425948073, -189.37600539314462, -184.40741894002085, -181.99597465340403, -175.9982441659755, -175.1124250821736, -172.81466
# 413704288, -168.24327711926674, -168.8542881173948, -165.58821956845412, -161.08514742785218, -158.68329193933226, -155.49406532273292, -151.90744757380716, -150.65247839644837, -152.0785992903316, -149.03039734276888, -146.79462707736
# 255, -145.96209453750626, -146.28837694683426, -147.04926846088884, -147.0529292833776, -143.23689770162304, -139.9732885863077, -135.39326549645477, -134.86474690459247, -137.7577523104391, -134.98250294341398, -133.92128316280616, -1
# 33.024293973543, -133.31317904292663, -132.93657263249617, -130.86638909392823, -131.08420668306553, -131.3925338286176, -131.06178824459155, -133.12492780511474, -133.36907343293169, -133.36346177692036, -133.86189056160345, -127.0743
# 2256237664, -127.11061823415321, -123.20582272845027, -121.34475784794296, -121.19439398358807, -119.99418630014439, -116.3955951633393, -119.84577106397211, -117.16348449181956, -118.51619447948414, -117.62143639341515, -117.596640196
# 79231, -115.52278585964694, -117.59924392857037, -116.4415059127918, -113.08705514305694, -113.36007729183653, -110.63906467791449, -111.14035116538082, -114.28514476378724, -116.8924896388991, -116.17061068645704, -116.80014490238132,
#  -116.6188643530337, -114.12338899602338, -113.46985834696834, -111.34762634855306, -110.3350267371424, -109.52660657223637, -109.73595591655409, -106.9084274638717, -108.38555413360075, -105.39176874092296, -100.96059337784402, -104.2
# 0532918429988, -101.42401006786994, -98.96141845365793, -100.70932223591385, -101.399340608454, -99.94123231406627, -92.59595239611157, -92.2531233372343, -91.91719390630223, -89.89155291607769, -85.31672487499092, -86.55920099532992,
# -85.71713440834395, -79.66017946869665, -79.4143282793391, -78.45915315206527, -77.78087861569784, -76.76947248524684, -75.61996261860392, -75.09930624605872, -73.68509137219226, -73.3965816015583, -72.87104777727168, -70.2128075831769
# 4, -61.85621199768817, -60.75037795431588, -57.380116180144114, -54.25014390681492, -47.44338815094387, -46.482387419781645, -43.57696721177746, -40.78301706340292, -36.3998030100167, -35.621979494264295, -34.54580386475642, -31.751229
# 72872587, -28.4896917190593, -28.358070832974935, -23.151976921395434, -16.310994861757468, -15.564540703620956, -11.78267631305613, -9.201396373418131, -1.0665611952245198, 2.3071323366632943, 1.1058540471560334, -0.19183804101588067,
#  5.311257359986218, 2.1419568971087166, 5.21884117597162, 9.36106228252644, 8.244126779237298, 11.22973450210835, 11.362680133251988, 11.876873193474408, 12.083346385969465, 12.699644871099208, 15.959660176365709, 19.809665265159126, 1
# 6.200379486025412, 15.484499915754249, 17.954727140185263, 17.58696302674323, 17.41574261248719, 17.16344791624963, 16.994202825960418, 16.35223331587163, 16.75848951803077, 15.228269974650537, 19.756312302957706, 21.66365293765607, 24
# .281572825725576, 28.838967956640477, 28.691487754954, 30.558978433806946, 32.97255953445765, 30.336038101359563, 29.05115053192364, 26.912613844912098, 25.856431952925867, 28.090491267413707, 28.490418292485273, 30.642662066585512, 32
# .05821322880552, 33.56451574641773, 31.686573853836016, 31.89130902399159, 36.30390289006102, 29.69368760402225, 29.909362009596908, 28.924338534425914, 31.23774876810285, 32.59185022185385, 33.51842295456218, 32.28543142596717, 30.170
# 849820565053, 32.3155152634049, 29.79384871073514, 33.1823902083534, 33.34577254508783, 34.97878361680497, 34.49026417706251, 31.63597568478708, 33.03736060296461, 37.878046809541964, 37.54827836687493, 39.60671639685237, 39.3766332675
# 9742, 38.59211628902113, 42.791189483804565, 42.013670602486066, 41.86720189290777, 45.27034816666457, 45.596317344376175, 46.50081493624008, 46.66743317032657, 50.64086632458904, 53.19116936670084, 55.255491797426295, 55.3988535927211
# 8, 56.409388132534296, 57.50359052234047, 55.74348482152888, 57.218405772513634, 55.51577296070358, 56.66733701696475, 55.82451470239133, 55.88724718348495, 56.737482507077345, 60.800852549987205, 67.5748689338018, 71.18238301371865, 7
# 1.15623596296714, 73.66199778276216, 80.43623338268853, 80.07094385722962, 84.2896346611058, 84.3001612631189, 82.5185969348266, 88.08011850388638, 91.17016673103491, 94.29400639464625, 97.24932579845012, 96.26500912468764, 96.25890024
# 35921, 97.58588549158729, 96.44669578889831, 99.31622623138632, 100.3235023681111, 98.5087006480311, 101.81830075484437, 108.06628681181117, 113.95108444247387, 114.82886563637884, 116.05509977124183, 116.43003556770067, 114.8572010469
# 3364, 117.6308012267033, 117.62234311617156, 122.63795247998819, 122.98351446802377, 121.95087134227384, 125.68671683530432, 123.8955537469281, 127.19966302733894, 127.69696354381261, 123.0107529878846, 126.4712013492438, 127.192328902
# 34598, 127.77700822723492, 126.54699055174687, 129.05010190687497, 129.65735038693066, 130.32644454159632, 132.64422828100393, 130.2310655607224, 131.63191375693648, 129.23441507186885, 126.96201712908281, 127.98594633505148, 131.72217
# 569512762, 131.56043256168664, 136.1352372713705, 134.63909863757016, 135.83710661841553, 135.04818849017528, 132.6725953986554, 132.70233295398796, 131.28362095052108, 131.87559163990088, 128.9299969765856, 127.50000667739987, 126.781
# 56028204384, 132.46780893863652, 130.67069896312105, 130.92505566890478, 127.88476429992454, 125.33697226354114, 124.62801473632727, 128.58105092786403, 126.91790755929222, 125.71073736954263, 128.35119698051497, 122.65402719527425, 12
# 4.16354477133211, 129.87602303529988, 131.85434998625385, 130.7443805833534, 130.2155986031655, 122.08133552660917, 121.7944108517042, 121.56959903176956, 122.51892899574413, 124.04772942043324, 129.53710672274732, 130.44720348452577,
# 140.035615657231, 138.7015583848748, 146.00993159355482, 147.34152300721163, 150.99738552473968, 151.65046910049628, 154.89581898234144, 153.5646402494872, 153.01166560090303, 153.4460320313791, 156.28844084784998, 161.4589427211716, 1
# 61.24662566331875, 163.23429234592516, 170.8581583882417, 175.44299745824767, 175.68601833766442, 173.04459640240077, 170.18945887815266, 172.23830674297866, 168.4468893465993, 167.8232431720531, 170.44335689636978, 169.94733567432996,
#  165.91326528741251, 167.53679940966143, 168.08601597606565, 171.18261418305596, 171.73348251008693, 172.6903494834611, 172.18733656358293, 171.43988002652696, 172.39416496110832, 171.67232780008328, 172.28998006922188, 169.99631294371
# 704, 173.10925179784732, 174.33096757020758, 172.732730532661, 176.3637058108129, 176.31533805857248, 173.13182880206008, 169.95855625224638, 171.47222509416275, 170.80813553941508, 169.78774609216353, 165.8092061071593, 164.4695676561
# 6153, 162.54396207808574, 161.94504587571723, 159.96210764946593, 157.89591903721208, 154.33652986843938, 153.42469210850734, 153.9988979018162, 154.30481668247128, 155.38124312802105, 154.2645522599056, 150.80864037160433, 154.5770596
# 6572, 151.90914038080268, 151.94296299567216, 148.88173910922663, 148.6422179210813, 148.50609506201744, 144.81112969045856, 143.9648786687699, 143.10114245469458, 146.96761348034386, 147.69392034313086, 145.0394331628188, 145.25331614
# 166788, 134.12759339129164, 133.29915120344845, 134.12923580576532, 136.62316915369985, 135.81095656008176, 127.65383225449509, 125.10417580902343, 124.16111563886487, 123.26795792373527, 113.10045592497443, 110.85960651395557, 96.3853
# 5840903427, 80.17115347423966, 82.23183149861656, 74.31676028752818, 66.20320231562681, 66.47478930445698, 48.97456321750179, 43.017436287766614, 35.31204351202208, 45.44540751099703, 44.38568544612524, 45.47007811724129, 52.1939694730
# 38315, 39.884551220594055, 44.792879756089626, 53.33948741815054, 55.06053164532925, 49.082305550344266, 42.93987602949881, 55.37956232132134, 70.59506441216219, 74.71834815541362, 55.39185100808599, 58.04082133486771, 50.7898751808570
# 1, 50.94517577661305, 56.9861524018127, 59.78996645660868, 47.29881858616777, 47.89479899493932, 53.08987287126183, 42.444198269625765, 27.120258003490527, 17.309638555141756, 7.9803215285983535, 14.54844796241465, 8.238266407609345, 4
# .12733039912492, 3.868675138222317, 5.338860392938065, 8.08099475811477, 5.481483365137662, -4.315416779077631, -0.004527395289120478, 8.565727232558846, 6.506188939461817, 1.6624664461491023, 2.5348486438443105, 3.3691735132880716, 1.
# 2739448496471892, -2.3275858471052295, -2.995351966521256, -13.36608098021113, -8.626424051890917, -5.238718983412005, -5.32534925994317, -10.797586315210934, 5.849719362511471, 23.967143701074356, 16.477761069372836, 6.842826939372276
# 5, 7.101018939619601, 5.7345587446428565, 3.734974553894164, 7.187832080255386, -1.5416606109810858, 7.279990174383402, -3.4854625040100364, -10.510733136360521, -17.67413828669339, -30.717298576061125, -35.50339627114553, -25.68150422
# 1990245, -26.6156693521895, -25.614934061515033, -30.218272039048298, -30.539095117021244, -29.191264918639654, -31.68680985812247, -35.709485340585346, -33.620708726347914, -41.106001797740504, -27.676028408551154, -34.20858702833075,
#  -44.53303744983853, -47.303469792971576, -38.466277470229564, -40.583444469235495, -29.186321569842963, -36.62614170023526, -22.575670781559182, -7.296329837388816, -15.345643999710655, -6.374723289710767, -15.542375020087531, -6.6313
# 73917712848, 1.33904258367107, 1.7030513511895777, 1.2764448283799712, 8.342741921969196, 13.33349456460401, 27.941836649693826, 20.688817586671213, 25.466053333186114, 30.99293961428384, 29.28018201374907, 29.262948179898626, 33.95714
# 500597627, 38.22165462188407, 39.648382968735895]





# plt.xlabel('num_agent_train_steps_per_iter')
# plt.ylabel('Eval_AverageReturn')
plt.plot(x, y_ant_train, 'b')


# plt.xlabel('n_iter')
# plt.ylabel('performance')
# plt.plot(x, y_ant_train, 'b', x, y_ant_eval, "r")
# plt.bar(x, height=y_ant_loss, width=0.3)

# fig, ax1 = plt.subplots()


# color = 'tab:blue'
# ax1.set_xlabel('n_iter')
# ax1.set_ylabel('mean performance', color=color)
# ax1.plot(x, y_hopper_train, 'g', label="train_mean")
# ax1.plot(x, y_hopper_eval, 'b', label="eval_mean")
# ax1.axhline(y=3772, color='r', label="expert mean", linestyle='-')
# ax1.axhline(y=442, color='y', label="behavior cloning", linestyle='-')
# ax1.tick_params(axis='y', labelcolor=color)
# plt.legend(loc="right")
#
# ax2 = ax1.twinx()
#
# color = 'tab:red'
# ax2.set_ylabel('eval loss', color=color)  # we already handled the x-label with ax1
# ax2.bar(x, height=y_hopper_loss, width=0.3, color=color)
# ax2.tick_params(axis='y', labelcolor=color)
#
# plt.title("Hopper DAgger")
# fig.tight_layout()


# t = np.arange(0., 5., 0.2)
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
#
# plt.bar([1, 2, 3, 4], height=[1, 4, 9, 16], width=0.3)


# plt.plot(t, t, 'b--', t, t**2, 'bs', t, t**3, 'g^')
# plt.ylabel('some numbers')
plt.show()