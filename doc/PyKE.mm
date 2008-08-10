<map version="0.8.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1216337861149" ID="Freemind_Link_1728048469" MODIFIED="1216340919190" TEXT="PyKE">
<node CREATED="1216344317502" ID="Freemind_Link_992866189" MODIFIED="1216344673489" POSITION="right" TEXT="knowledge_bases">
<node CREATED="1216349750377" ID="Freemind_Link_642607403" MODIFIED="1216349754488" TEXT="what is a knowledge base?"/>
<node CREATED="1216344326486" ID="Freemind_Link_966234231" MODIFIED="1216347063895" TEXT="fact_bases">
<node CREATED="1216347086839" ID="Freemind_Link_1219857088" MODIFIED="1216347091646" TEXT="what is a fact?"/>
<node CREATED="1216347065712" ID="Freemind_Link_543127937" MODIFIED="1216347531310" TEXT="universal facts"/>
<node CREATED="1216347070472" ID="Freemind_Link_1205187763" MODIFIED="1216347537421" TEXT="case_specific facts"/>
<node CREATED="1216347104159" ID="Freemind_Link_1881520302" MODIFIED="1216350047209" TEXT="order of fact lookups on backtracking"/>
<node CREATED="1216347113546" ID="Freemind_Link_1462096531" MODIFIED="1216347127795" TEXT="internal caching"/>
<node CREATED="1218304709453" ID="Freemind_Link_1473399794" MODIFIED="1218304718635" TEXT=".kfb files">
<node CREATED="1218304720638" ID="Freemind_Link_978809075" MODIFIED="1218304728066" TEXT="syntax"/>
<node CREATED="1218304728862" ID="Freemind_Link_629711865" MODIFIED="1218304843526" TEXT="loading">
<arrowlink DESTINATION="Freemind_Link_1276213100" ENDARROW="Default" ENDINCLINATION="560;0;" ID="Freemind_Arrow_Link_1700490932" STARTARROW="None" STARTINCLINATION="560;0;"/>
<node CREATED="1218304762552" ID="Freemind_Link_129808086" MODIFIED="1218304778338" TEXT="compiles .kfb files into .fbc files and loads them"/>
<node CREATED="1218304780609" ID="Freemind_Link_17233504" MODIFIED="1218304785515" TEXT="compiling is automatic"/>
</node>
</node>
</node>
<node CREATED="1216344330554" ID="Freemind_Link_1164789183" MODIFIED="1216344685790" TEXT="rule_base">
<node CREATED="1216344429510" ID="Freemind_Link_789541104" MODIFIED="1216347050249" TEXT="rules">
<node CREATED="1216344445969" FOLDED="true" ID="Freemind_Link_1386265889" MODIFIED="1216349683141" TEXT="what is a rule?">
<node CREATED="1216344459585" ID="Freemind_Link_1289750371" MODIFIED="1216344463748" TEXT="premise">
<node CREATED="1216348668190" ID="Freemind_Link_535629107" MODIFIED="1216348694690" TEXT="fact (or goal)">
<node CREATED="1216348579353" ID="Freemind_Link_967760767" MODIFIED="1216348583287" TEXT="syntax"/>
<node CREATED="1216349167393" ID="Freemind_Link_597853457" MODIFIED="1216349192833" TEXT="can omit knowledge_base name in backward chaining rule to mean the same rule base category"/>
<node CREATED="1216349270453" ID="Freemind_Link_1076090962" MODIFIED="1216349286428" TEXT="plan spec options for backward chaining rules"/>
</node>
<node CREATED="1216348631295" ID="Freemind_Link_1957604401" MODIFIED="1216348634558" TEXT="first">
<node CREATED="1216348783533" ID="Freemind_Link_671075587" MODIFIED="1216348786412" TEXT="syntax"/>
<node CREATED="1216350085931" ID="Freemind_Link_697947671" MODIFIED="1216350092275" TEXT="always fails on backtracking"/>
</node>
<node CREATED="1216348635219" ID="Freemind_Link_819670818" MODIFIED="1216348639527" TEXT="forall/require">
<node CREATED="1216348792029" ID="Freemind_Link_198331692" MODIFIED="1216348800409" TEXT="syntax"/>
<node CREATED="1216350104578" ID="Freemind_Link_56112484" MODIFIED="1216350109792" TEXT="always fails on backtracking"/>
</node>
<node CREATED="1216348640099" ID="Freemind_Link_1457962340" MODIFIED="1216348644386" TEXT="notany">
<node CREATED="1216348803540" ID="Freemind_Link_330875505" MODIFIED="1216348805870" TEXT="syntax"/>
<node CREATED="1216350118721" ID="Freemind_Link_1204416892" MODIFIED="1216350123448" TEXT="always fails on backtracking"/>
</node>
<node CREATED="1216348645087" ID="Freemind_Link_166058387" MODIFIED="1216348648953" TEXT="python premise">
<node CREATED="1216348808036" ID="Freemind_Link_411400529" MODIFIED="1216348834946" TEXT="matching a python expression to a pattern">
<node CREATED="1216350128493" ID="Freemind_Link_1925515887" MODIFIED="1216350136359" TEXT="always fails on backtracking"/>
</node>
<node CREATED="1216348835871" ID="Freemind_Link_1723219604" MODIFIED="1216350269903" TEXT="successively matching the output of a python iteratable to a pattern (through backtracking)"/>
<node CREATED="1216348882965" ID="Freemind_Link_1393235903" MODIFIED="1216348899622" TEXT="checking a python expression">
<node CREATED="1216350141940" ID="Freemind_Link_1496233885" MODIFIED="1216350148889" TEXT="always fails on backtracking"/>
</node>
<node CREATED="1216348900596" ID="Freemind_Link_64431340" MODIFIED="1216348944352" TEXT="python statements">
<arrowlink DESTINATION="Freemind_Link_1508747959" ENDARROW="Default" ENDINCLINATION="122;0;" ID="Freemind_Arrow_Link_1419289429" STARTARROW="None" STARTINCLINATION="122;0;"/>
<node CREATED="1216350168263" ID="Freemind_Link_1604340723" MODIFIED="1216350178464" TEXT="always fail on backtracking"/>
</node>
</node>
<node CREATED="1216349004684" ID="Freemind_Link_245871546" MODIFIED="1216349559996" TEXT="! to throw an AssertionError if the premise fails">
<node CREATED="1216349069513" ID="Freemind_Link_1736387291" MODIFIED="1216349077786" TEXT="only applies to backward chaining rules"/>
<node CREATED="1216349079033" ID="Freemind_Link_554380968" MODIFIED="1216349109733" TEXT="can only be used with facts (or goals) and the &quot;first&quot; clause"/>
</node>
<node CREATED="1216349438554" ID="Freemind_Link_1780110978" MODIFIED="1216349889815" TEXT="how a set of premises are executed with backtracking"/>
</node>
<node CREATED="1216344464752" ID="Freemind_Link_1205265273" MODIFIED="1216344467321" TEXT="conclusion">
<node CREATED="1216348720803" ID="Freemind_Link_61673050" MODIFIED="1216348729021" TEXT="fact (or goal)">
<node CREATED="1216348716776" ID="Freemind_Link_677307575" MODIFIED="1216348719586" TEXT="syntax"/>
<node CREATED="1216349141662" ID="Freemind_Link_1870658464" MODIFIED="1216349160378" TEXT="must not specify a knowledge_base name in backward chaining rule"/>
</node>
<node CREATED="1216348729535" ID="Freemind_Link_1508747959" MODIFIED="1216348944350" TEXT="python statements">
<node CREATED="1216348969581" ID="Freemind_Link_24517564" MODIFIED="1216348971758" TEXT="syntax"/>
<node CREATED="1216348741799" ID="Freemind_Link_786012543" MODIFIED="1216348990763" TEXT="only for forward chaining rules in conclusion"/>
</node>
</node>
</node>
<node CREATED="1216340996413" FOLDED="true" ID="Freemind_Link_1143553684" MODIFIED="1216341005193" TEXT="forward chaining">
<node CREATED="1216347450244" ID="Freemind_Link_1722643312" MODIFIED="1216347457396" TEXT="meaning of forward chaining"/>
<node CREATED="1216343898380" ID="Freemind_Link_1894415000" MODIFIED="1216343899948" TEXT="syntax"/>
<node CREATED="1216344300931" ID="Freemind_Link_176387521" MODIFIED="1216347431293" TEXT="executed at rule base activation time">
<arrowlink DESTINATION="Freemind_Link_1986125832" ENDARROW="Default" ENDINCLINATION="743;0;" ID="Freemind_Arrow_Link_777029345" STARTARROW="None" STARTINCLINATION="743;0;"/>
</node>
<node CREATED="1216343916627" ID="Freemind_Link_612565815" MODIFIED="1216343921312" TEXT="order of rule execution">
<node CREATED="1216347367716" ID="Freemind_Link_874515916" MODIFIED="1216347384196" TEXT="re-running past rules when new facts are established"/>
<node CREATED="1216345766522" ID="Freemind_Link_1192632119" MODIFIED="1216345780217" TEXT="with rule_base inheritance"/>
</node>
<node CREATED="1216344545021" ID="Freemind_Link_594823406" MODIFIED="1216344566831" TEXT="executed until no more rules match the facts"/>
<node CREATED="1216344569260" ID="Freemind_Link_215945546" MODIFIED="1216344576768" TEXT="can&apos;t call backward chaining rules"/>
<node CREATED="1216343922135" ID="Freemind_Link_1026827877" MODIFIED="1216343924925" TEXT="fc_extras"/>
<node CREATED="1216347142817" ID="Freemind_Link_1925528799" MODIFIED="1216347145705" TEXT="uses">
<node CREATED="1216347148005" ID="Freemind_Link_1142957502" MODIFIED="1216347155019" TEXT="data driven applications"/>
<node CREATED="1216347155805" ID="Freemind_Link_661659513" MODIFIED="1216347297967" TEXT="derive many possible outputs from a small set of possible inputs"/>
</node>
</node>
<node CREATED="1216341006320" FOLDED="true" ID="Freemind_Link_1860230711" MODIFIED="1216341009330" TEXT="backward chaining">
<node CREATED="1216347463872" ID="Freemind_Link_1134438709" MODIFIED="1216379621997" TEXT="meaning of backward chaining"/>
<node CREATED="1216343902956" ID="Freemind_Link_298526575" MODIFIED="1216343905175" TEXT="syntax"/>
<node CREATED="1216347582335" ID="Freemind_Link_841683200" MODIFIED="1216347607620" TEXT="executed when your program calls for a proof">
<arrowlink DESTINATION="Freemind_Link_1512457251" ENDARROW="Default" ENDINCLINATION="614;0;" ID="Freemind_Arrow_Link_1491499769" STARTARROW="None" STARTINCLINATION="614;0;"/>
</node>
<node CREATED="1216349803334" ID="Freemind_Link_1195752787" MODIFIED="1216349813137" TEXT="backtracking tries next rule with the same goal">
<node CREATED="1216343927807" ID="Freemind_Link_918709987" MODIFIED="1216343932344" TEXT="order of rule execution">
<node CREATED="1216345784682" ID="Freemind_Link_556661358" MODIFIED="1216345792556" TEXT="with rule_base inheritance"/>
</node>
<node CREATED="1216350408857" ID="Freemind_Link_1190098993" MODIFIED="1216350420072" TEXT="this is how plan functions are selected"/>
</node>
<node CREATED="1216343933170" ID="Freemind_Link_719967781" MODIFIED="1216343940451" TEXT="bc_extras"/>
<node CREATED="1216343948370" ID="Freemind_Link_1805482337" MODIFIED="1216343950437" TEXT="plans">
<node CREATED="1216350447788" ID="Freemind_Link_322993713" MODIFIED="1216350686144" TEXT="each backward chaining goal may produce a plan (a python function with all of its needed subfunctions, and all of their needed subfunctions, etc, connected into a complete call graph)">
<node CREATED="1216347671447" ID="Freemind_Link_157111339" MODIFIED="1216348248085" TEXT="called like an ordinary python function">
<arrowlink DESTINATION="Freemind_Link_337994704" ENDARROW="Default" ENDINCLINATION="716;0;" ID="Freemind_Arrow_Link_1252059067" STARTARROW="None" STARTINCLINATION="716;0;"/>
</node>
</node>
<node CREATED="1216344032627" ID="Freemind_Link_1606334968" MODIFIED="1216344038508" TEXT="can be reused"/>
<node CREATED="1216344039250" ID="Freemind_Link_1725972934" MODIFIED="1216347897465" TEXT="can be pickled">
<node CREATED="1216347786686" ID="Freemind_Link_1461777546" MODIFIED="1216347839189" TEXT="as a long-term cache for subsequent runs of the same program"/>
<node CREATED="1216347851944" ID="Freemind_Link_1769546602" MODIFIED="1216347990027" TEXT="as a plan compiler to load compiled plans into a second program">
<node CREATED="1216344045182" ID="Freemind_Link_1920317287" MODIFIED="1216347965352" TEXT="second program only needs pyke.immutable_dict"/>
</node>
</node>
<node CREATED="1216344076816" ID="Freemind_Link_25696395" MODIFIED="1216348031540" TEXT="pattern variables in python code"/>
<node CREATED="1216344086524" ID="Freemind_Link_1478362219" MODIFIED="1216348065527" TEXT="handling plans returned from subgoals">
<node CREATED="1216344114831" ID="Freemind_Link_1604163075" MODIFIED="1216344129637" TEXT="indented line w/$$">
<node CREATED="1216344147794" ID="Freemind_Link_649824076" MODIFIED="1216344152930" TEXT="optional step clause"/>
<node CREATED="1216349330750" ID="Freemind_Link_989240092" MODIFIED="1216349348665" TEXT="automatically added to front of &quot;with&quot; clause"/>
</node>
<node CREATED="1216344131830" ID="Freemind_Link_1519490989" MODIFIED="1216348181125" TEXT="as pattern variable">
<font NAME="SansSerif" SIZE="12"/>
<node CREATED="1216349354765" ID="Freemind_Link_522138352" MODIFIED="1216349360601" TEXT="not run automatically"/>
</node>
<node CREATED="1216347621565" ID="Freemind_Link_544758986" MODIFIED="1216350567851" TEXT="this is how required subfunctions are selected"/>
</node>
<node CREATED="1216343957177" ID="Freemind_Link_804026284" MODIFIED="1216343961172" TEXT="plan_extras"/>
<node CREATED="1216343970289" ID="Freemind_Link_636827291" MODIFIED="1216343972352" TEXT="uses">
<node CREATED="1216344182380" ID="Freemind_Link_585404279" MODIFIED="1216344267870" TEXT="postpone execution of critical code until after all rules are satisfied">
<node CREATED="1216344202251" ID="Freemind_Link_1315617180" MODIFIED="1216349403587" TEXT="database updates"/>
<node CREATED="1216343989612" ID="Freemind_Link_1626547479" MODIFIED="1216344012618" TEXT="create a network of objects"/>
</node>
<node CREATED="1216343975805" ID="Freemind_Link_1992382459" MODIFIED="1216350918302" TEXT="for better performance by running complicated decision making code once and then reusing the resultant code many times"/>
</node>
</node>
<node CREATED="1216347239581" ID="Freemind_Link_518303895" MODIFIED="1216347241024" TEXT="uses">
<node CREATED="1216347242921" ID="Freemind_Link_1442076055" MODIFIED="1216347257110" TEXT="goal directed applications"/>
<node CREATED="1216347259068" ID="Freemind_Link_724166562" MODIFIED="1216347290564" TEXT="derive a small set of possible outputs from a large set of possible inputs"/>
</node>
</node>
</node>
<node CREATED="1216345691397" ID="Freemind_Link_406481726" MODIFIED="1216345694620" TEXT="inheritance">
<node CREATED="1216345714508" ID="Freemind_Link_1456899267" MODIFIED="1216345737027" TEXT="rule_base category"/>
<node CREATED="1216345806205" ID="Freemind_Link_921909056" MODIFIED="1216345913415" TEXT="excluding certain backward chaining goals from being inherited"/>
</node>
<node CREATED="1216344501827" ID="Freemind_Link_1097298780" MODIFIED="1216344505754" TEXT=".krb files">
<node CREATED="1216344508223" ID="Freemind_Link_1405186303" MODIFIED="1216344512287" TEXT="syntax"/>
<node CREATED="1216344513182" ID="Freemind_Link_1263748171" MODIFIED="1218140848077" TEXT="loading">
<arrowlink DESTINATION="Freemind_Link_1276213100" ENDARROW="Default" ENDINCLINATION="279;0;" ID="Freemind_Arrow_Link_300472352" STARTARROW="None" STARTINCLINATION="283;0;"/>
<node CREATED="1216351049591" ID="Freemind_Link_119885790" MODIFIED="1216351064097" TEXT="compiles .krb files into .py files and imports them">
<node CREATED="1216351019408" ID="Freemind_Link_1032561609" MODIFIED="1216351082472" TEXT="may create up to 3 .py files for each .krb file"/>
</node>
<node CREATED="1216344615142" ID="Freemind_Link_110148392" MODIFIED="1216344621535" TEXT="compiling is automatic">
<node CREATED="1216344623230" ID="Freemind_Link_1428680401" MODIFIED="1216348528219" TEXT="but doesn&apos;t automatically recompile until you create a new engine"/>
</node>
</node>
<node CREATED="1216344524982" ID="Freemind_Link_632300396" MODIFIED="1218140862268" TEXT="activating">
<arrowlink DESTINATION="Freemind_Link_1986125832" ENDARROW="Default" ENDINCLINATION="607;0;" ID="Freemind_Arrow_Link_1994817685" STARTARROW="None" STARTINCLINATION="237;0;"/>
</node>
</node>
</node>
<node CREATED="1218139126663" ID="Freemind_Link_60612906" MODIFIED="1218139209969" TEXT="question_base">
<node CREATED="1218140412372" ID="Freemind_Link_1554332733" MODIFIED="1218140435431" TEXT="parameters to the question">
<node CREATED="1218140437438" ID="Freemind_Link_1894803745" MODIFIED="1218140443935" TEXT="must be bound to values"/>
<node CREATED="1218140444602" ID="Freemind_Link_1097054958" MODIFIED="1218140476839" TEXT="can be substituted into any of the strings within the question using the string.Template syntax"/>
</node>
<node CREATED="1218139799829" ID="Freemind_Link_1392961051" MODIFIED="1218139809080" TEXT="different types of answers">
<node CREATED="1218139810173" ID="Freemind_Link_1774414842" MODIFIED="1218139815022" TEXT="yes/no"/>
<node CREATED="1218139816526" ID="Freemind_Link_566975389" MODIFIED="1218139820291" TEXT="integer"/>
<node CREATED="1218139820826" ID="Freemind_Link_1388595763" MODIFIED="1218139822791" TEXT="float"/>
<node CREATED="1218139823134" ID="Freemind_Link_1641317110" MODIFIED="1218139825370" TEXT="number"/>
<node CREATED="1218139825742" ID="Freemind_Link_474144842" MODIFIED="1218139827016" TEXT="string"/>
<node CREATED="1218139841347" ID="Freemind_Link_1861112634" MODIFIED="1218139847756" TEXT="select_1"/>
<node CREATED="1218139848511" ID="Freemind_Link_1916349070" MODIFIED="1218139851710" TEXT="select_n"/>
</node>
<node CREATED="1218140725504" ID="Freemind_Link_514714444" MODIFIED="1218140735150" TEXT="answer parameter pattern matched to user&apos;s answer"/>
<node CREATED="1218139653681" ID="Freemind_Link_93233211" MODIFIED="1218139662613" TEXT="answers are cached">
<node CREATED="1218140069335" ID="Freemind_Link_250848438" MODIFIED="1218140078717" TEXT="cache is cleared when the engine is reset"/>
</node>
<node CREATED="1218139737726" ID="Freemind_Link_1301762436" MODIFIED="1218139751141" TEXT="there are different ways to interact with the user">
<node CREATED="1218139759823" ID="Freemind_Link_133726390" MODIFIED="1218139765261" TEXT="ask_tty.py"/>
<node CREATED="1218139765975" ID="Freemind_Link_1872833123" MODIFIED="1218139777394" TEXT="ask_wx.py"/>
<node CREATED="1218139898206" ID="Freemind_Link_377878420" MODIFIED="1218140025787" TEXT="install imported module as &apos;ask_module&apos; attr on either the question_base or knowledge_engine"/>
<node CREATED="1218139982958" ID="Freemind_Link_1533737315" MODIFIED="1218140001412" TEXT="ask_tty used by default"/>
<node CREATED="1218140037893" ID="Freemind_Link_1582940550" MODIFIED="1218140046298" TEXT="write your own user interaction module"/>
</node>
<node CREATED="1218139248420" ID="Freemind_Link_488439990" MODIFIED="1218139257659" TEXT=".kqb files">
<node CREATED="1218139288514" ID="Freemind_Link_57525613" MODIFIED="1218139291434" TEXT="syntax"/>
<node CREATED="1218139292291" ID="Freemind_Link_71067801" MODIFIED="1218140693643" TEXT="loading">
<arrowlink DESTINATION="Freemind_Link_1276213100" ENDARROW="Default" ENDINCLINATION="250;0;" ID="Freemind_Arrow_Link_907901968" STARTARROW="None" STARTINCLINATION="250;0;"/>
<node CREATED="1218139307035" ID="Freemind_Link_1003909038" MODIFIED="1218139402732" TEXT="compiles .kqb files into .qbc files and loads them"/>
<node CREATED="1218139403708" ID="Freemind_Link_1500460340" MODIFIED="1218139414395" TEXT="compiling is automatic"/>
</node>
</node>
</node>
<node CREATED="1216344334118" ID="Freemind_Link_1390316986" MODIFIED="1216344336134" TEXT="special">
<node CREATED="1216344338210" ID="Freemind_Link_1610274213" MODIFIED="1216344340970" TEXT="claim_goal"/>
<node CREATED="1216399527584" ID="Freemind_Link_903145835" MODIFIED="1216399531618" TEXT="check_command"/>
<node CREATED="1216399547323" ID="Freemind_Link_898803219" MODIFIED="1216399548807" TEXT="command"/>
<node CREATED="1216399549663" ID="Freemind_Link_754192557" MODIFIED="1216399553247" TEXT="general_command"/>
</node>
<node CREATED="1216344389627" ID="Freemind_Link_1405755691" MODIFIED="1216344396678" TEXT="extensibility"/>
</node>
<node CREATED="1216344651505" ID="Freemind_Link_1899970365" MODIFIED="1216344655448" POSITION="right" TEXT="knowledge_engine">
<node CREATED="1216346098936" ID="Freemind_Link_260781230" MODIFIED="1216346117753" TEXT="calling pyke from your python program">
<node CREATED="1216346120712" ID="Freemind_Link_1927215817" MODIFIED="1216346129694" TEXT="from pyke import knowledge_engine"/>
<node CREATED="1216346130771" ID="Freemind_Link_1276213100" MODIFIED="1218304843524" TEXT="engine = knowledge_engine.engine"/>
<node CREATED="1216346149886" ID="Freemind_Link_60846124" MODIFIED="1216347531311" TEXT="engine.add_universal_fact">
<arrowlink DESTINATION="Freemind_Link_543127937" ENDARROW="Default" ENDINCLINATION="308;0;" ID="Freemind_Arrow_Link_1575801102" STARTARROW="None" STARTINCLINATION="308;0;"/>
</node>
<node CREATED="1216346354730" ID="Freemind_Link_479242288" MODIFIED="1216346357385" TEXT="loop">
<node CREATED="1216346177181" ID="Freemind_Link_420213469" MODIFIED="1216347537422" TEXT="engine.add_case_specific_fact">
<arrowlink DESTINATION="Freemind_Link_1205187763" ENDARROW="Default" ENDINCLINATION="347;0;" ID="Freemind_Arrow_Link_1758290041" STARTARROW="None" STARTINCLINATION="347;0;"/>
</node>
<node CREATED="1216346195280" ID="Freemind_Link_1986125832" MODIFIED="1218140862269" TEXT="engine.activate"/>
<node CREATED="1216346259246" ID="Freemind_Link_1512457251" MODIFIED="1216347607618" TEXT="engine.prove_1">
<node CREATED="1216346300384" ID="Freemind_Link_1690844986" MODIFIED="1216346301829" TEXT="or">
<node CREATED="1216346264790" ID="Freemind_Link_1012312061" MODIFIED="1216346269899" TEXT="engine.prove_n"/>
<node CREATED="1216346250206" ID="Freemind_Link_1466984125" MODIFIED="1216346257360" TEXT="engine.prove"/>
</node>
</node>
<node CREATED="1216346314263" ID="Freemind_Link_337994704" MODIFIED="1216348248083" TEXT="execute the resulting plan"/>
<node CREATED="1216346142339" ID="Freemind_Link_1277930996" MODIFIED="1216346234533" TEXT="engine.reset">
<node CREATED="1216346984516" ID="Freemind_Link_1736249616" MODIFIED="1216347005770" TEXT="deletes case_specific_facts from fact_bases"/>
<node CREATED="1218156314912" ID="Freemind_Link_287522236" MODIFIED="1218156348852" TEXT="clears all question caches in question_bases"/>
</node>
</node>
<node CREATED="1216346416407" ID="Freemind_Link_429646996" MODIFIED="1216346420422" TEXT="other functions">
<node CREATED="1216346421483" ID="Freemind_Link_834242035" MODIFIED="1216346815202" TEXT="engine.print_stats (since last engine.reset())"/>
<node CREATED="1216346426579" ID="Freemind_Link_1511055573" MODIFIED="1216346823277" TEXT="engine.trace/engine.untrace"/>
<node CREATED="1216346497952" ID="Freemind_Link_999685498" MODIFIED="1216346505771" TEXT="from pyke import krb_traceback">
<node CREATED="1216346538614" ID="Freemind_Link_16466392" MODIFIED="1216346546823" TEXT="krb_traceback.print_exc()"/>
</node>
<node CREATED="1216346827694" ID="Freemind_Link_673839188" MODIFIED="1216346829027" TEXT="test"/>
</node>
</node>
<node CREATED="1216346784340" ID="Freemind_Link_1250792142" MODIFIED="1216346912593" TEXT="you can have multiple instances of knowledge_engines using different knowledge bases"/>
</node>
<node CREATED="1218155730538" ID="Freemind_Link_1229838546" MODIFIED="1218155733278" POSITION="right" TEXT="examples"/>
<node CREATED="1218156083292" ID="Freemind_Link_1612320530" MODIFIED="1218156084954" POSITION="right" TEXT="internals"/>
<node CREATED="1218158071230" ID="Freemind_Link_765757853" MODIFIED="1218305116895" POSITION="left" TEXT="what can PyKE do for me?"/>
<node CREATED="1218158086351" ID="Freemind_Link_173254572" MODIFIED="1218158118140" POSITION="left" TEXT="what are the drawbacks of using PyKE?"/>
<node CREATED="1218155965474" ID="Freemind_Link_1667004899" MODIFIED="1218155966923" POSITION="left" TEXT="features">
<node CREATED="1218156645449" ID="Freemind_Link_742432311" MODIFIED="1218156660700" TEXT="both forward-chaining and backward-chaining"/>
<node CREATED="1218156716548" ID="Freemind_Link_763574843" MODIFIED="1218156731033" TEXT="may be embedded within any python program"/>
<node CREATED="1218157179808" ID="Freemind_Link_1120441624" MODIFIED="1218157191008" TEXT="may include python code snippets within the rules"/>
<node CREATED="1218156744590" FOLDED="true" ID="Freemind_Link_310654415" MODIFIED="1218156768796" TEXT="can automatically assemble python functions into complete call graphs">
<node CREATED="1218156787400" ID="Freemind_Link_1268182560" MODIFIED="1218156802843" TEXT="by attaching the python functions to backward-chaining rules"/>
<node CREATED="1218156815697" ID="Freemind_Link_1885293879" MODIFIED="1218156917313" TEXT="unlike other approaches to code reuse, ensures that each function&apos;s requirements are met before executing any of them"/>
<node CREATED="1218157004871" ID="Freemind_Link_1279278164" MODIFIED="1218157022053" TEXT="calls the completed function call graph a &quot;plan&quot;"/>
<node CREATED="1218157041953" ID="Freemind_Link_47552201" MODIFIED="1218157066619" TEXT="plans may be run many times without needing to re-run pyke"/>
<node CREATED="1218157068246" ID="Freemind_Link_142901827" MODIFIED="1218157083084" TEXT="plans may be pickled and sent to other processes or stored to disk"/>
<node CREATED="1218157084279" ID="Freemind_Link_1349362240" MODIFIED="1218157098392" TEXT="only one small pyke module is required to load the pickle"/>
<node CREATED="1218156944716" ID="Freemind_Link_1596811970" MODIFIED="1218156951899" TEXT="this is an optional feature"/>
</node>
<node CREATED="1218157109001" ID="Freemind_Link_787059190" MODIFIED="1218157340706" TEXT="can question end users from the rules"/>
<node CREATED="1218157275225" ID="Freemind_Link_798815092" MODIFIED="1218157321373" TEXT="can run programs from rules to snif the system"/>
<node CREATED="1218157394565" ID="Freemind_Link_651997872" MODIFIED="1218157458873" TEXT="you can write your own kind of knowledge_bases to do whatever you want to prove a statement"/>
</node>
<node CREATED="1218155783604" ID="Freemind_Link_284948023" MODIFIED="1218155787090" POSITION="left" TEXT="installation"/>
<node CREATED="1216351264518" FOLDED="true" ID="Freemind_Link_962996702" MODIFIED="1216379092527" POSITION="left" TEXT="overview" VSHIFT="-38">
<node CREATED="1216351454194" ID="Freemind_Link_1372986928" MODIFIED="1216353623800" TEXT="knowledge is made up of simple statements of fact">
<node CREATED="1216353582405" ID="Freemind_Link_1164028160" MODIFIED="1216353588521" TEXT="what a statement of fact looks like"/>
<node CREATED="1216353698333" ID="Freemind_Link_1749934684" MODIFIED="1216353746826" TEXT="like rows in a relational table, there is never a need to record the same statement of fact twice"/>
</node>
<node CREATED="1216351665913" FOLDED="true" ID="Freemind_Link_335695136" MODIFIED="1216353352576" TEXT="new statements can be dynamically deduced from already known statements through if-then rules">
<node CREATED="1216353983049" ID="Freemind_Link_28863524" MODIFIED="1216356044007" TEXT="if premises; then conclusions"/>
<node CREATED="1216356046859" ID="Freemind_Link_946233064" MODIFIED="1216356072076" TEXT="each premise and conclusion is a statement pattern that may match multiple statements of fact"/>
<node CREATED="1216351284825" ID="Freemind_Link_1467107537" MODIFIED="1216355428584" TEXT="pyke tries all combinations of these matching statements in order to satisfy the &quot;if&quot; part of the rule">
<node CREATED="1216355325441" ID="Freemind_Link_1113116109" MODIFIED="1216355346490" TEXT="this is done using a process called backtracking"/>
<node CREATED="1216355350036" ID="Freemind_Link_1190400047" MODIFIED="1216356099409" TEXT="the &quot;if&quot; part of the rule is made up of a list of premises"/>
<node CREATED="1216355374091" ID="Freemind_Link_268719589" MODIFIED="1216356114546" TEXT="as pyke tries each premise, the premise may succeed or fail"/>
<node CREATED="1216355461883" ID="Freemind_Link_786073464" MODIFIED="1216356125772" TEXT="if the premise succeeds, pyke tries the next premise"/>
<node CREATED="1216356540244" ID="Freemind_Link_215847141" MODIFIED="1216356550137" TEXT="if the premise fails, pyke backtracks to the previous premise and sees if there is another matching statement for it"/>
<node CREATED="1216355474903" ID="Freemind_Link_1572406493" MODIFIED="1216356563202" TEXT="this attempt at finding another matching statement may also succeed or fail, and pyke repeats the process, always going down to the next premise on success and backtracking up to the prior premise on failure"/>
<node CREATED="1216356585585" ID="Freemind_Link_793973591" MODIFIED="1216356607721" TEXT="the process continues moving up and down the list of premises until one of two things happen:"/>
<node CREATED="1216356369030" ID="Freemind_Link_483876832" MODIFIED="1216356912468" TEXT="the last premise succeeds, there is no premise to move down to and so the rule succeeds.  In this case the rule&apos;s conclusions are then known to be additional statements of facts."/>
<node CREATED="1216356421775" ID="Freemind_Link_541306312" MODIFIED="1216356874874" TEXT="the first premise fails, there is no premise to move up to and so the rule fails"/>
<node CREATED="1216355623721" ID="Freemind_Link_232499739" MODIFIED="1216356772250" TEXT="thus, each premise may be run from two directions: from above to find the first matching statement of fact when the prior premise succeeds; and from below to find the next matching statement of fact when the following premise fails."/>
<node CREATED="1216355955719" ID="Freemind_Link_1941152892" MODIFIED="1216356367638" TEXT="to talk about how premises behave in both of these cases, we say &quot;the premise does X, and on backtracking does Y&quot;.  This means that the premise does X when entered from above and Y when returned to from below."/>
</node>
</node>
<node CREATED="1216351725131" ID="Freemind_Link_1378286275" MODIFIED="1216353372307" TEXT="comparing this to normal programming, which is made up of data and code that operates on that data; the statements are the data, and the if-then rules are the code that operates on that data"/>
<node CREATED="1216351278981" ID="Freemind_Link_813440882" MODIFIED="1216353162554" TEXT="statements are grouped into knowledge bases">
<node CREATED="1216353167031" ID="Freemind_Link_1120526718" MODIFIED="1216353181690" TEXT="simple statements asserted by your python program"/>
<node CREATED="1216353183346" ID="Freemind_Link_1227491090" MODIFIED="1216353401325" TEXT="statements deduced or deducable by the if-then rules"/>
</node>
<node CREATED="1216351272069" ID="Freemind_Link_1042910921" MODIFIED="1216353966895" TEXT="the code that rubs the statements and if-then rules together is called a knowledge engine">
<node CREATED="1216353419588" ID="Freemind_Link_1193654355" MODIFIED="1216353490455" TEXT="pyke implements the knowledge engine as a python class so that you can have multiple instances running different knowledge bases for different purposes"/>
</node>
<node CREATED="1216353803660" ID="Freemind_Link_491564855" MODIFIED="1216353807906" TEXT="integration with python"/>
</node>
<node CREATED="1216340762982" ID="Freemind_Link_563953999" MODIFIED="1218157770527" POSITION="left" TEXT="pattern matching" VSHIFT="-6">
<node CREATED="1216338038124" HGAP="24" ID="_" MODIFIED="1216379082256" TEXT="patterns" VSHIFT="-9">
<node CREATED="1216338045115" ID="Freemind_Link_1076679700" MODIFIED="1216338385098" TEXT="pattern literals">
<arrowlink DESTINATION="Freemind_Link_735183346" ENDARROW="Default" ENDINCLINATION="176;0;" ID="Freemind_Arrow_Link_575361317" STARTARROW="None" STARTINCLINATION="176;0;"/>
<node CREATED="1216338719943" ID="Freemind_Link_1135314767" MODIFIED="1216338722554" TEXT="syntax">
<node CREATED="1216338785404" ID="Freemind_Link_1304330716" MODIFIED="1216338788383" TEXT="None"/>
<node CREATED="1216338789620" ID="Freemind_Link_918687483" MODIFIED="1216338792390" TEXT="True/False"/>
<node CREATED="1216338793196" ID="Freemind_Link_22976935" MODIFIED="1216338797104" TEXT="numbers"/>
<node CREATED="1216338797800" ID="Freemind_Link_1947112081" MODIFIED="1216338814688" TEXT="strings (with python quoting style)"/>
<node CREATED="1216338728091" ID="Freemind_Link_864701450" MODIFIED="1216339161931" TEXT="identifier is string shortcut"/>
<node CREATED="1216338847646" ID="Freemind_Link_318797678" MODIFIED="1216338863920" TEXT="tuples">
<arrowlink DESTINATION="Freemind_Link_1767893880" ENDARROW="Default" ENDINCLINATION="214;0;" ID="Freemind_Arrow_Link_16435665" STARTARROW="None" STARTINCLINATION="214;0;"/>
</node>
</node>
</node>
<node CREATED="1216338062367" ID="Freemind_Link_1356934076" MODIFIED="1216339396776" TEXT="pattern variables">
<arrowlink DESTINATION="Freemind_Link_735183346" ENDARROW="Default" ENDINCLINATION="147;0;" ID="Freemind_Arrow_Link_1833625773" STARTARROW="None" STARTINCLINATION="147;0;"/>
<node CREATED="1216338079262" ID="Freemind_Link_1781964505" MODIFIED="1216338083649" TEXT="syntax"/>
<node CREATED="1216338097481" ID="Freemind_Link_1635641664" MODIFIED="1216338101386" TEXT="scope"/>
<node CREATED="1216338094329" ID="Freemind_Link_569383253" MODIFIED="1216338096659" TEXT="binding"/>
<node CREATED="1216338086097" ID="Freemind_Link_897349738" MODIFIED="1216338338960" TEXT="anonymous variables"/>
</node>
<node CREATED="1216338069386" ID="Freemind_Link_962501181" MODIFIED="1216338412241" TEXT="tuple patterns">
<arrowlink DESTINATION="Freemind_Link_735183346" ENDARROW="Default" ENDINCLINATION="106;0;" ID="Freemind_Arrow_Link_860827115" STARTARROW="None" STARTINCLINATION="106;0;"/>
<node CREATED="1216338655326" ID="Freemind_Link_208374357" MODIFIED="1216338661736" TEXT="syntax">
<node CREATED="1216338745766" ID="Freemind_Link_1767893880" MODIFIED="1216338863917" TEXT="no comma needed for singleton tuples"/>
</node>
<node CREATED="1216338662522" ID="Freemind_Link_250842875" MODIFIED="1216338681995" TEXT="&quot;rest&quot; pattern variable">
<node CREATED="1216339091148" ID="Freemind_Link_1700240172" MODIFIED="1216339103555" TEXT="always binds to a (possibly empty) tuple"/>
</node>
</node>
</node>
<node CREATED="1216338202161" HGAP="22" ID="Freemind_Link_735183346" MODIFIED="1216379078432" TEXT="matching" VSHIFT="-10">
<node CREATED="1216338183365" ID="Freemind_Link_886490123" MODIFIED="1216339448532" TEXT="matching a pattern to data"/>
<node CREATED="1216338190281" ID="Freemind_Link_1291025340" MODIFIED="1216339441095" TEXT="matching two patterns together"/>
</node>
<node CREATED="1216338904785" HGAP="29" ID="Freemind_Link_320168827" MODIFIED="1216379073057" TEXT="uses" VSHIFT="-34">
<node CREATED="1216338909207" ID="Freemind_Link_155121629" MODIFIED="1216339307302" TEXT="decompose tuples"/>
<node CREATED="1216338924719" ID="Freemind_Link_1571060928" MODIFIED="1216339314237" TEXT="construct tuples"/>
<node CREATED="1216339325974" ID="Freemind_Link_1585594894" MODIFIED="1216339339473" TEXT="pass data forward"/>
<node CREATED="1216339340025" ID="Freemind_Link_1269938364" MODIFIED="1216339344025" TEXT="pass data backwards"/>
</node>
</node>
</node>
</map>
