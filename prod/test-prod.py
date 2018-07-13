import pymysql
import datetime
import tushare as ts

lows = [[0, "300243"], [0, "300076"], [0, "603086"], [0, "603811"], [2, "002872"], [0, "300444"], [0, "300497"], [1, "603067"], [1, "002370"], [1, "600380"], [1, "300310"], [1, "002435"], [1, "000786"], [0, "000636"], [0, "603993"], [1, "300423"], [1, "300485"], [1, "002463"], [0, "600511"], [0, "002110"], [0, "002889"], [1, "002225"], [1, "002138"], [1, "603128"], [1, "002484"], [1, "600009"], [0, "002798"], [0, "002510"], [0, "002867"], [1, "300219"], [1, "603456"], [1, "603826"], [1, "300038"], [1, "002137"], [1, "002645"], [0, "603108"], [1, "300182"], [1, "603345"], [1, "300081"], [1, "600351"], [0, "002563"], [1, "600586"], [1, "002349"], [0, "603197"], [0, "600619"], [0, "600596"], [0, "300326"], [1, "603669"], [1, "002406"], [2, "600093"], [1, "002601"], [1, "002879"], [776, "002164"], [1, "600295"], [0, "002600"], [2, "300232"], [1, "002842"], [1, "600260"], [1, "000785"], [0, "002737"], [2, "603535"], [1, "603976"], [0, "603708"], [0, "300237"], [1, "601003"], [0, "000089"], [1, "600634"], [1, "600782"], [1, "600507"], [1, "002701"], [1, "600285"], [1, "002875"], [1, "000413"], [2, "600227"], [2, "601021"], [2, "002788"], [0, "002462"], [2, "603987"], [1, "600419"], [2, "300621"], [1, "603225"], [2, "300507"], [0, "002056"], [1, "600216"], [1, "002444"], [1, "000717"], [0, "300340"], [1, "002626"], [1, "601689"], [1, "002470"], [1, "600781"], [1, "601965"], [2, "000560"], [1, "600346"], [1, "600585"], [0, "002430"], [2, "300200"], [1, "601100"], [2, "000657"], [1, "000516"], [1, "603823"], [1, "000910"], [1, "000062"], [2, "600367"], [1, "603828"], [239, "002882"], [338, "600029"], [0, "000338"], [1, "300296"], [0, "600305"], [1, "603788"], [1, "600590"], [1, "600761"], [2, "300335"], [605, "002766"], [2, "600278"], [2, "300300"], [0, "600569"], [0, "002340"], [2, "002283"], [1, "603116"], [2, "300206"], [1, "300349"], [2, "603689"], [1, "600004"], [0, "300439"], [1, "603663"], [0, "300344"], [2, "000672"], [1, "600126"], [3, "002756"], [0, "600426"], [1, "600282"], [1, "600138"], [1, "000932"], [2, "000830"], [2, "002345"], [0, "600535"], [1, "603181"], [1, "603567"], [2, "000043"], [2, "000028"], [1, "002511"], [1, "002050"], [2, "603611"], [1, "000739"], [2, "600103"], [1, "002223"], [1, "002742"], [1, "002303"], [2, "000519"], [3, "300292"], [2, "600613"], [2, "002317"], [1, "300233"], [2, "601139"], [2, "002565"], [0, "002360"], [2, "603668"], [2, "601857"], [1, "000887"], [1, "002832"], [11, "002235"], [1, "601006"], [0, "600729"], [286, "002118"], [1, "600011"], [1, "300580"], [2, "002091"], [0, "002422"], [1, "601233"], [1, "300437"], [1, "002176"], [2216, "600819"], [404, "603203"], [1, "000513"], [2, "600050"], [2, "600648"], [3, "603639"], [1, "600814"], [1, "600572"], [2, "603357"], [2, "002672"], [326, "601111"], [127, "002078"], [4, "300501"], [2, "603928"], [0, "600566"], [0, "300428"], [2, "603113"], [2, "603787"], [2, "002392"], [2, "000488"], [2, "000708"], [2, "603601"], [0, "002823"], [2, "600231"], [2, "600808"], [2, "600612"], [2, "603037"], [2, "002295"], [3, "603458"], [2, "603380"], [3, "300221"], [841, "600328"], [2, "002865"], [2, "600917"], [1, "300599"], [0, "300298"], [2, "603887"], [42, "002637"], [2, "603369"], [2, "002440"], [1, "300272"], [2, "603358"], [2, "000921"], [2, "600028"], [1, "002233"], [2, "002398"], [2, "002267"], [2, "002860"], [977, "000060"], [1, "002559"], [2, "603319"], [2, "002040"], [2, "600229"], [2, "000756"], [2, "600487"], [1, "603608"], [2, "000582"], [611, "600452"], [0, "603117"], [1, "600329"], [2, "300016"], [3, "603626"], [1, "002603"], [2, "000898"], [3, "603226"], [1, "601168"], [2, "300351"], [2, "002822"], [0, "002386"], [2, "600389"], [8, "601018"], [2, "000902"], [3, "600859"], [2, "000753"], [0, "600160"], [2, "000828"], [2, "300316"], [8, "002582"], [3, "000850"], [2, "600143"], [1, "002557"], [2, "600697"], [0, "600141"], [2, "002753"], [0, "603368"], [1014, "002117"], [2, "601677"], [2, "002707"], [2, "002068"], [0, "002081"], [2, "603585"], [918, "002071"], [1, "600529"], [1, "000553"], [2, "600755"], [2, "600738"], [2, "600650"], [1, "000552"], [0, "600136"], [8, "600778"], [2, "600284"], [2, "600888"], [2, "601216"], [2, "600352"], [2, "002685"], [3, "600854"], [4, "300547"], [506, "000960"], [126, "603518"], [2, "002009"], [2, "002419"], [3, "002093"], [2, "002635"], [2, "300184"], [0, "603268"], [15, "600577"], [927, "603308"], [2, "600018"], [2, "002811"], [12, "002320"], [2, "600594"], [2, "600075"], [2, "603359"], [13, "603817"], [0, "002381"], [3, "300035"], [2, "600970"], [0, "002709"], [2, "600803"], [2, "600387"], [2, "000951"], [1, "300026"], [15, "601918"], [0, "600176"], [2, "300396"], [761, "601717"], [2, "300434"], [2, "000683"], [3, "002109"], [2, "002019"], [1, "600195"], [2, "300127"], [2, "000875"], [5, "601225"], [15, "600477"], [3, "000922"], [2, "603017"], [553, "002491"], [2, "000860"], [2, "300121"], [2, "000419"], [96, "002173"], [2, "002290"], [0, "002365"], [13, "002763"], [6, "000551"], [801, "600502"], [14, "600101"], [2, "600170"], [1, "600270"], [0, "000703"], [2, "002424"], [375, "603298"], [2, "600420"], [3, "000761"], [352, "002843"], [13, "002061"], [3, "002401"], [1, "002088"], [1, "600897"], [2, "600031"], [2, "600658"], [1, "601579"], [2, "300622"], [0, "002493"], [2, "603566"], [1, "002140"], [2, "000789"], [444, "600710"], [2, "300178"], [2, "600737"], [3, "300255"], [3, "600589"], [2, "002762"], [3, "603393"], [2, "002728"], [2, "000528"], [8, "603878"], [13, "603768"], [2, "300438"], [84, "603008"], [1, "300398"], [8, "002649"], [2, "002084"], [682, "603030"], [832, "002503"], [2, "603416"], [2, "600062"], [867, "600798"], [0, "603026"], [2, "002001"], [2, "002062"], [3, "600382"], [97, "600114"], [2, "603015"], [726, "603223"], [2, "601001"], [2, "000421"], [2, "603101"], [0, "300488"], [2, "002529"], [3, "603578"], [3, "601000"], [2, "002251"], [0, "600754"], [915, "600057"], [2, "000906"], [2, "600098"], [2, "600846"], [848, "600963"], [881, "603166"], [2, "002020"], [532, "000155"], [0, "600828"], [2, "000069"], [3, "002651"], [309, "601228"], [2, "002587"], [804, "600603"], [2, "300041"], [2, "603528"], [2, "603808"], [0, "000650"], [2, "600741"], [3, "002393"], [2, "000937"], [2, "600655"], [11, "600618"], [8, "000407"], [3, "300058"], [3, "600027"], [8, "002769"], [8, "300427"], [963, "002060"], [2, "601636"], [1, "600600"], [2, "002258"], [884, "002478"], [2, "600479"], [12, "600630"], [2, "002158"], [2, "002318"], [3, "002094"], [2, "002029"], [808, "000505"], [8, "002640"], [1, "600801"], [2, "600557"], [2, "600010"], [2, "600190"], [2, "603855"], [2, "000049"], [0, "002299"], [3, "300270"], [2, "603938"], [2, "600592"], [658, "002343"], [2, "000826"], [0, "600563"], [2, "002391"], [2, "300329"], [2, "600578"], [2, "600059"], [2, "000813"], [2, "601515"], [0, "603885"], [2, "600516"], [15, "300635"], [2, "300563"], [0, "002154"], [239, "002042"], [11, "300385"], [2, "300082"], [3, "603508"], [2, "000680"], [0, "600273"], [2, "600674"], [2, "600125"], [3, "600497"], [2, "600997"], [13, "300262"], [8, "603196"], [642, "600153"], [3, "002566"], [680, "603599"], [3, "600513"], [1, "002727"], [2, "300199"], [2, "600283"], [0, "601607"], [3, "002546"], [748, "000032"], [2218, "002243"], [2, "603023"], [0, "002404"], [2, "603877"], [217, "601326"], [2, "002203"], [2, "600820"], [4, "600780"], [3, "000050"], [3, "002187"], [3, "000726"], [2, "603998"], [8, "002619"], [2, "002597"], [3, "601333"], [2, "600256"], [3, "603385"], [0, "300144"], [2, "002377"], [0, "600104"], [0, "600201"], [820, "000411"], [276, "600362"], [997, "600317"], [1193, "300273"], [2, "600705"], [2, "000983"], [2, "601368"], [2, "601898"], [11, "300421"], [3, "600308"], [0, "603569"], [2, "600713"], [0, "002711"], [2, "601933"], [3, "000861"], [3, "002429"], [2, "600996"], [0, "600939"], [2, "000423"], [2, "600580"], [10, "600805"], [1963, "002375"], [3, "002818"], [318, "603179"], [6, "601801"], [39, "600681"], [795, "600297"], [2, "603338"], [685, "300473"], [507, "600219"], [13, "300190"], [3, "300165"], [3, "603798"], [9, "002776"], [8, "600744"], [2, "000952"], [2, "601311"], [1030, "002574"], [270, "601011"], [0, "002407"], [3, "002139"], [40, "600236"], [2, "002482"], [13, "002472"], [3, "000966"], [2, "300119"], [250, "600691"], [2, "600522"], [1, "002269"], [3, "600395"], [0, "603609"], [2, "603618"], [625, "002770"], [3, "600794"], [2, "600309"], [0, "603730"], [11, "002852"], [0, "600377"], [2, "002613"], [2, "601618"], [0, "600017"], [3, "002526"], [558, "600499"], [97, "601117"], [893, "300387"], [970, "600163"], [301, "603081"], [3, "002513"], [2, "002242"], [942, "000958"], [3, "002446"], [2, "600508"], [859, "601789"], [721, "601238"], [3, "002325"], [2, "000617"], [822, "002734"], [569, "601688"], [2, "600973"], [0, "600323"], [490, "603299"], [9, "300418"], [53, "600977"], [63, "000425"], [569, "600998"], [8, "300068"], [505, "601611"], [2, "603018"], [72, "002632"], [246, "002884"], [2, "300180"], [3, "300467"], [840, "000524"], [2, "000883"], [876, "601186"], [922, "603100"], [3, "603002"], [2, "300006"], [2, "603198"], [767, "603968"], [668, "000040"], [3, "600076"], [3, "002425"], [801, "600528"], [7, "300261"], [868, "000058"], [1041, "000833"], [2, "300476"], [13, "600475"], [9, "300017"], [2068, "600090"], [977, "000702"], [946, "000417"], [2, "300039"], [628, "002335"], [11, "600602"], [3, "603123"], [3, "300481"], [8, "600969"], [2, "300095"], [458, "601369"], [749, "002183"], [2, "000818"], [3, "002245"], [8, "000705"], [485, "002695"], [272, "601015"], [2, "300258"], [3, "300094"], [96, "300422"], [2, "000999"], [1192, "002186"], [8, "002298"], [3, "002215"], [3, "600330"], [8, "300044"], [2, "002620"], [2806, "600875"], [2, "600886"], [985, "002541"], [2, "002191"], [11, "300410"], [8, "002781"], [2, "603306"], [885, "603009"], [1189, "000665"], [2, "601699"], [2, "300207"], [775, "300446"], [2, "600740"], [15, "002717"], [0, "603667"], [2, "002543"], [896, "601788"], [3, "600789"], [2, "600233"], [2, "000597"], [0, "002661"], [2, "600060"], [2, "002275"], [97, "300246"], [3, "600030"], [55, "603997"], [0, "603686"], [0, "603558"], [0, "603012"], [0, "601727"], [4, "601668"], [1, "601390"], [8, "601005"], [1350, "600831"], [907, "600811"], [3, "600795"], [0, "600750"], [891, "600723"], [86, "600711"], [2, "600702"], [0, "600687"], [3, "600643"], [2, "600408"], [0, "600398"], [12, "600397"], [0, "600293"], [2, "600248"], [1, "600221"], [1, "600217"], [1066, "600168"], [2, "600167"], [3, "300459"], [672, "300388"], [0, "300324"], [0, "300320"], [8, "300286"], [3, "300217"], [0, "300146"], [606, "300118"], [1, "300108"], [2, "300079"], [13, "300057"], [209, "002716"], [740, "002682"], [78, "002668"], [406, "002617"], [3, "002612"], [47, "002602"], [2, "002598"], [756, "002573"], [13, "002561"], [3, "002556"], [13, "002535"], [2, "002533"], [17, "002464"], [2, "002456"], [304, "002450"], [2, "002412"], [80, "002408"], [3, "002328"], [2, "002293"], [2, "002206"], [1, "002171"], [0, "002102"], [8, "002097"], [0, "002051"], [2, "002022"], [2, "002014"], [0, "002011"], [2, "000967"], [3, "000903"], [308, "000889"], [0, "000825"], [0, "000723"], [1400, "000669"], [899, "000603"], [1305, "000598"], [13, "000563"], [11, "000426"], [3, "000166"], [1188, "000156"], [3, "000100"], [670, "000055"], [354, "000034"], [6, "002034"], [0, "600884"], [583, "002712"], [10, "603033"], [2, "000525"], [2, "601799"], [296, "600388"], [2, "002536"], [2, "002327"], [3, "603167"], [466, "300441"], [669, "600785"], [9, "002745"], [5, "600900"], [3, "600064"], [0, "600483"], [770, "300287"], [3, "000606"], [8, "300007"], [6, "002667"], [5, "002757"], [2, "300305"], [1197, "002416"], [2, "601800"], [1215, "300195"], [43, "600337"], [5, "002228"], [2054, "002255"], [3, "300150"], [3, "002344"], [0, "000989"], [11, "300020"], [6, "601900"], [768, "600869"], [2, "300031"], [6, "000543"], [302, "601366"], [2, "000858"], [3, "300297"], [463, "000157"], [327, "603665"], [3, "601996"], [12, "600369"], [2, "002426"], [3, "600007"], [236, "601899"], [53, "601566"], [2, "002111"], [6, "600978"], [3, "002608"], [311, "000429"], [3, "601127"], [893, "300406"], [3, "603919"], [3, "300625"], [2, "002438"], [2, "000651"], [2, "600348"], [2, "601188"], [1105, "000715"], [3, "300447"], [2, "002537"], [2, "600690"], [3, "600736"], [3, "300307"], [548, "000821"], [2, "002455"], [958, "000026"], [728, "002514"], [3, "600706"], [3, "600251"], [3, "002280"], [3, "300323"], [93, "000676"], [3, "300021"], [487, "600548"], [2, "002540"], [3, "000880"], [0, "300284"], [6, "002697"], [825, "601567"], [2, "601601"], [13, "000980"], [3, "002104"], [764, "603111"], [741, "603979"], [1421, "300289"], [7, "600567"], [2, "600802"], [3, "002550"], [3, "601336"], [1085, "300295"], [15, "000030"], [537, "002654"], [11, "603035"], [0, "600197"], [0, "002126"], [630, "002085"], [3, "300138"], [2, "600518"], [962, "600439"], [2, "600332"], [0, "603806"], [507, "002221"], [14, "600039"], [455, "002217"], [723, "000662"], [8, "300046"], [3, "000070"], [2, "300511"], [10, "601908"], [6, "600179"], [26, "600403"], [3, "601016"], [319, "002128"], [0, "002442"], [556, "600491"], [842, "002366"], [6, "600277"], [1208, "002064"], [3, "000848"], [3, "300113"], [15, "300376"], [3, "000961"], [686, "601886"], [6, "002449"], [11, "300098"], [2, "601669"], [3, "600629"], [7, "600461"], [675, "002706"], [1404, "002447"], [2, "603839"], [3, "600131"], [0, "002585"], [8, "300512"], [3, "601952"], [135, "601678"], [6, "300537"], [602, "300145"], [2, "002531"], [8, "300086"], [514, "002726"], [13, "600666"], [914, "600327"], [2, "600486"], [2, "600299"], [0, "300606"], [3, "000333"], [3, "300120"], [8, "600845"], [2, "601318"], [11, "002195"], [6, "300528"], [539, "600987"], [2, "002468"], [721, "002087"], [828, "603600"], [883, "002686"], [5, "600547"], [1760, "002481"], [2674, "600858"], [2, "300596"], [13, "300027"], [9, "600081"], [683, "002509"], [193, "601877"], [2, "002080"], [3, "600438"], [81, "300247"], [2, "002397"], [8, "000547"], [702, "002247"], [1251, "002638"], [5, "000591"], [914, "300064"], [13, "002562"], [2, "603757"], [46, "000799"], [0, "601633"], [0, "002768"], [0, "000713"], [0, "300283"], [4, "002238"], [12, "002400"], [8, "300383"], [378, "002508"], [982, "603555"], [805, "000078"], [0, "600598"], [206, "601012"], [0, "002772"], [816, "000063"], [1192, "002277"], [520, "002721"], [938, "300274"], [12, "002376"], [890, "000498"], [164, "000022"], [0, "603843"]]

lows.sort(reverse=True)

print(lows)
