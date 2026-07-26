import json

# Read existing data
with open('/Users/ma/.openclaw/workspace/smart-home-news-data/data.json', 'r') as f:
    data = json.load(f)

existing_news = data['news']
existing_titles = {n['title'] for n in existing_news}

# Today's new news (2026-07-26)
new_news = [
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "Shelly Gen4全系确认支持Matter over Thread，年内全面推送",
        "summary": "智能家居设备厂商Shelly官方确认，Gen4全系设备将通过固件更新支持Matter over Thread协议。Gen4内置ESP32-C6芯片已具备硬件基础，官方社区投票仅涉及实现细节而非功能本身。固件将从9月开始分批推送，预计年底前完成全系覆盖。此举将大幅扩充Thread生态设备阵容，推动Matter协议互联互通加速落地。",
        "source": "Stadt Bremerhaven",
        "url": "https://stadt-bremerhaven.de/shelly-alle-gen4-geraete-werden-ein-update-auf-matter-over-thread-erhalten/",
        "keywords": ["Shelly", "Matter over Thread", "Thread协议", "智能家居", "设备互联"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "Aqara Power Plug H2 EU发布：同时支持Matter over Thread和Zigbee双协议",
        "summary": "绿米（Aqara）在欧洲推出Power Plug H2 EU智能插座，是少数同时支持Matter over Thread和Zigbee两种协议的设备。这一双协议设计让用户可以在Thread mesh网络和传统Zigbee网络中自由选择，兼顾未来升级需求和现有设备兼容性问题。",
        "source": "Stadt Bremerhaven",
        "url": "https://stadt-bremerhaven.de/aqara-power-plug-h2-eu-neuer-zwischenstecker-unterstuetzt-matter-over-thread-und-zigbee/",
        "keywords": ["Aqara", "Matter over Thread", "Zigbee", "智能插座", "Thread协议"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "亿道发布Ailyn AI中枢：WAIC 2026软硬一体化平台让智能贯通所有设备",
        "summary": "智能计算设备领域领先企业亿道（Emdoor）在WAIC 2026上正式发布Ailyn，一款软硬一体化的AI中枢平台。本届大会以\"万物智联，边缘无界\"为主题，Ailyn可实现多设备间的智能贯通，基于多年在云端、边缘端、终端设备及可穿戴形态领域的积累，推动边缘AI在智能家居场景的真正落地。",
        "source": "China Newswire",
        "url": "https://mediatcb.com/news/20260720/19720/",
        "keywords": ["亿道", "Ailyn", "AI中枢", "WAIC", "边缘AI", "智能家居"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "从\"模型竞争\"迈向\"产业落地\"：边缘智能催生算力架构新变革",
        "summary": "WAIC 2026期间，边缘智能（Edge AI）成为产业界关注热点。具身智能、智能制造、智能汽车等新兴领域集中亮相，业内普遍认为随着AI不断向终端侧延伸，边缘计算已从辅助能力逐步发展为AI基础设施的重要组成部分，围绕实时计算、数据处理和系统协同的新型算力架构正在加快形成。",
        "source": "网易订阅",
        "url": "https://www.163.com/dy/article/L29R997R055040N3.html",
        "keywords": ["边缘AI", "端云协同", "WAIC", "具身智能", "智能家居"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "Home Assistant热议智能家居Agent化：开源平台能否成为终局？",
        "summary": "36氪深度分析Home Assistant平台的AI化路径，指出当前智能家居\"拉闸\"现象的根本原因在于大量设备的\"智能服务\"依赖品牌云端服务器运行，而非本地化处理。Agent化后的空调能告诉系统当前模式、温度变化、能耗情况，甚至能与摄像头联动自动调整风向。美的、海尔、Aqara、华为、涂鸦等国内品牌均在探索各自的Agent化路径，智能家居正从\"被动服务\"走向\"主动响应\"。",
        "source": "36氪",
        "url": "https://36kr.com/p/3865205179955846",
        "keywords": ["Home Assistant", "AI Agent", "智能家居", "本地化", "开源"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "policy",
        "categoryLabel": "政策标准",
        "title": "北京新增10类智能家居产品纳入以旧换新补贴，含具身智能机器人",
        "summary": "7月23日，北京市商务局发布公告，新增智能门锁、智能摄像头、智能扫地机（含智能洗地机、智能吸尘器）、智能马桶（含智能马桶盖）、数码相机、智能耳机、全屋智能主机、智能床、智能电动轮椅、具身智能机器人等10类产品纳入以旧换新补贴范围。具身智能机器人涵盖陪伴类机器人、机器狗、外骨骼机器人、养老照护机器人等产品，补贴标准为售价15%，单件最高1500元。",
        "source": "新京报",
        "url": "https://www.bjnews.com.cn/detail/1784863654019480.html",
        "keywords": ["北京补贴", "智能家居", "具身机器人", "以旧换新", "适老化"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "policy",
        "categoryLabel": "政策标准",
        "title": "福州扩大2026年智能家居购新补贴：新增数码相机、智能洗碗机等5类产品",
        "summary": "福州市商务局公告扩大2026年智能家居产品购新补贴范围，从7月22日起实施，有效期至今年12月31日。新增5类产品包括数码相机、智能洗碗机等，按最终销售价格15%给予补贴，每人每类可补贴1件，每件上限1500元。",
        "source": "福州新闻网",
        "url": "https://news.fznews.com.cn/fzyw/20260723/73Y31pk5DL.shtml",
        "keywords": ["福州补贴", "智能家居", "购新补贴", "数码相机", "洗碗机"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "policy",
        "categoryLabel": "政策标准",
        "title": "2026上半年国补带动消费1.1万亿，京东全面承接线上线下补贴落地",
        "summary": "商务部数据显示，2026年上半年，消费品以旧换新累计带动相关商品销售额1.1万亿元，惠及1.5亿人次，其中家电以旧换新6326.6万台，数码和智能产品购新7909.8万台。19个地方实施自主品类补贴政策，带动相关商品销售99.2万件，京东第一时间全面承接国补落地，支持智能机器人、净水器、智能马桶等地方自主品类补贴。",
        "source": "快科技",
        "url": "https://news.mydrivers.com/1/1138/1138883.htm",
        "keywords": ["国补", "以旧换新", "京东", "智能家居补贴", "消费"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "policy",
        "categoryLabel": "政策标准",
        "title": "北京\"立减补贴\"模式落地：消费者需通过\"京通\"实人认证领取资格券码",
        "summary": "北京市商务局明确新增10类智能家居补贴采用\"立减补贴\"模式，消费者须通过\"京通\"移动端完成实人认证后，进入\"智能家居补贴\"专区按需领用补贴资格券码，通过政策参与企业购买产品时于订单支付环节享受立减补贴，线上线下消费享受同等力度。享受补贴的产品须拆封核验与销售订单一致。",
        "source": "新浪科技",
        "url": "https://finance.sina.com.cn/tech/roll/2026-07-24/doc-iniixnfw9277669.shtml",
        "keywords": ["北京补贴", "立减补贴", "京通", "实人认证", "智能家居"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "小度发布家庭智能体中枢系统：适配全家庭成员多设备智能协同",
        "summary": "WAIC 2026期间，小度发布的家庭智能体中枢系统给出适配全家庭成员、多设备智能协同的解决方案。2026年上半年小米、华为等密集发布家庭智能体产品，海尔、美的等传统家电龙头宣布战略转型，AI家电一季度渗透率突破50%。",
        "source": "钛媒体",
        "url": "https://www.tmtpost.com/8068255.html",
        "keywords": ["小度", "家庭智能体", "多Agent协同", "智能家居", "WAIC"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "小米超级小爱同学：AI大模型+跨端多指令+6000+设备生态整合",
        "summary": "小米超级小爱同学基于AI大模型实现跨端多指令控制，接入米家6000+设备生态，成为统一指挥中心。小米/米家生态用户可实现一句话控制全家设备。但超级小爱的核心优势依托米家生态，苹果/华为HomeKit用户兼容性和联动深度会大打折扣。",
        "source": "新浪新闻",
        "url": "https://k.sina.com.cn/article_7879777294_1d5abdc0e06801v94k.html?from=tech",
        "keywords": ["小米", "超级小爱", "米家", "AI大模型", "全屋智能"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "全屋定制进入AI智能体时代：从\"被动指令\"到\"主动服务\"的交互革命",
        "summary": "2026年7月，全屋定制装修与智能家居已从单品控制进化为以AI智能体为核心的\"零操作自主居家\"生态。业主在规划阶段需同步完成水电预埋、网络覆盖与七大核心系统的一体化设计，海尔L4级智能体家电Seeker套系等已实现从\"听指令\"到\"主动服务\"的跨越。",
        "source": "新浪新闻",
        "url": "https://k.sina.com.cn/article_7880068385_1d5b04d2106801nhia.html?from=home",
        "keywords": ["全屋定制", "AI智能体", "智能家居", "主动服务", "空间革命"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "傅利叶发布康养机器人居家场景方案，GR-3完成全流程操作演示",
        "summary": "WAIC 2026期间，傅利叶在展台搭建完整居家场景，GR-3人形机器人完成取物、递送、安防巡检等任务，观众可用自然语言下达指令自主完成全流程操作。同期发布首款轮式双臂机器人GRW，适配康养照护等高负载人机协同场景。",
        "source": "机器人大讲堂",
        "url": "https://www.leaderobot.com/news/8549",
        "keywords": ["傅利叶", "人形机器人", "康养机器人", "WAIC", "智慧养老"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "面壁智能×乐聚机器人发布两款Agent方案：纯端侧运行成亮点",
        "summary": "WAIC 2026期间，面壁智能联合乐聚机器人发布展厅导览Agent和园区巡检Agent两款解决方案，前者可在无网环境下纯端侧运行导览系统，实时理解展厅环境并规划导览路线；后者可识别车辆违停、路面异常等。面壁智能还开源了MiniCPM-Robot系列模型，包括通用VLA模型RobotManip和移动跟踪模型RobotTrack。",
        "source": "产业家",
        "url": "https://www.163.com/dy/article/L2CKUOQT053179F1.html",
        "keywords": ["面壁智能", "乐聚机器人", "端侧AI", "具身智能", "WAIC"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "scenario",
        "categoryLabel": "场景落地",
        "title": "青岛探路智慧养老：毫米波跌倒检测、海信陪伴机器人率先落地",
        "summary": "青岛市在智慧养老领域率先探索，搭载毫米波监测与智能视觉技术的居家关爱机器人，能在识别老人跌倒时即刻触发预警，从识别异常到推送警报至家属手机全程不过数秒。海信联合青岛数据集团、中国移动研发的适老化智能陪伴机器人已落地应用。",
        "source": "腾讯新闻",
        "url": "https://news.qq.com/rain/a/20260705A0490S00",
        "keywords": ["智慧养老", "适老化", "毫米波雷达", "跌倒检测", "青岛", "海信"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "scenario",
        "categoryLabel": "场景落地",
        "title": "清雷科技获数千万Pre-A轮融资：毫米波雷达+AI切入医疗养老",
        "summary": "将雷达智能感知技术应用于AI辅助医疗、养老等民用领域的清雷科技宣布完成数千万Pre-A轮融资。清雷毫米波雷达产品与京东健康合作，将睡眠监测用于\"京东家医\"服务，面向睡眠障碍用户。其智慧养老SaaS系统已落地多家养老机构，实现非接触式老人健康监测与跌倒报警。",
        "source": "36氪",
        "url": "https://36kr.com/p/1440973085870979",
        "keywords": ["清雷科技", "毫米波雷达", "智慧养老", "跌倒检测", "融资"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "scenario",
        "categoryLabel": "场景落地",
        "title": "具身智能从展台走向产线：208款终端、超300台真机亮相WAIC",
        "summary": "WAIC 2026特设具身智能专属展区，展示208款具身智能终端、超300台真机。宇树科技、智元、傅利叶等多家企业展出的人形机器人已开始在工厂、仓储物流、商业服务等真实场景上岗，面向家庭场景的消费级机器人也成为重要方向，行业已从\"要不要做机器人\"走到\"做什么样的机器人\"阶段。",
        "source": "新浪科技",
        "url": "https://finance.sina.com.cn/tech/roll/2026-07-20/doc-iniimzfz3033040.shtml",
        "keywords": ["具身智能", "人形机器人", "WAIC", "量产", "场景落地"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "日本NICT警告：家庭IoT设备被滥用为住宅代理攻击节点，每日最多2.7万IP",
        "summary": "日本信息通信研究机构（NICT）与总务省、警察厅联合发布警告，家庭用IoT设备正被广泛滥用为\"住宅代理（Residential Proxy）\"攻击节点，用于隐藏攻击者所在、规避安全检测。调查发现2024年互联网银行诈骗中至少1918件（被害额约28.9亿日元）使用了住宅代理技术。NICT呼吁用户不使用来源不明的视频设备和VPN，定期更新设备固件。",
        "source": "NICT日本信息通信研究机构",
        "url": "https://www.nict.go.jp/press/2026/07/21-1.html",
        "keywords": ["IoT安全", "住宅代理", "NICT", "网络安全", "智能家居"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "毫米波雷达技术突破：无需摄像头即可感知人体活动，破解隐私与安防矛盾",
        "summary": "毫米波雷达技术在智能家居场景中实现突破，可在无需摄像头的情况下感知人体活动、监测跌倒，适用于隐私敏感场景（养老院、医院）的监控以及智能家居的智能感知，突破了隐私保护与智能监控之间的矛盾，成为家庭安防的新选择。",
        "source": "中华网",
        "url": "https://tech.china.com/articles/20260716/202607161918790.html",
        "keywords": ["毫米波雷达", "隐私保护", "智能感知", "跌倒检测", "智能家居"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "2026智能家居隐私指南：Matter、Zigbee和Thread如何保护家庭数据",
        "summary": "Smart Home Wizards发布2026智能家居隐私全面指南，分析Matter、Zigbee和Thread协议在家庭数据保护方面的差异。智能家居设备持续在后台收集行为数据，用户需了解各协议的安全性差异并采取相应保护措施，Matter协议在跨平台互操作性方面具有优势但数据保护仍需用户主动管理。",
        "source": "Smart Home Wizards",
        "url": "https://smarthomewizards.com/smart-home-privacy-concerns-2026-a-comprehensive-guide-to-protecting-your-data/",
        "keywords": ["智能家居", "隐私保护", "Matter", "Thread", "Zigbee", "数据安全"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "2026年最佳家庭安全系统：ADT、SimpliSafe和Vivint领先",
        "summary": "根据SafeHome.org评测，2026年最佳家庭安全系统为ADT、SimpliSafe和Vivint。ADT提供最佳安装服务，SimpliSafe在防盗保护方面领先，Vivint在智能家居集成方面表现最强。家庭安全系统正成为智能家居生态的核心组成部分，同时隐私与安全的平衡也成为选购重要考量。",
        "source": "SafeHome.org",
        "url": "https://www.safehome.org/security-systems/best/",
        "keywords": ["家庭安全系统", "智能安防", "ADT", "SimpliSafe", "Vivint"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "华为昇腾Atlas 950超节点真机首秀：业界最大规模1024卡超节点",
        "summary": "WAIC 2026开幕当天，华为昇腾950超节点（Atlas 950 SuperPoD）真机首次公开亮相，这是目前业界最大规模1024卡超节点产品，依托自研灵衢2.0全光互联协议，以单柜64卡为基础，可扩展至8192张NPU高速互联，支持万亿参数大模型训练与推理，为Agentic AI时代构建新一代算力底座。",
        "source": "ZAKER新闻",
        "url": "https://app.myzaker.com/news/article.php?pk=6a5f05018e9f094a4b0ff643",
        "keywords": ["华为", "昇腾950", "超节点", "WAIC", "AI芯片", "国产算力"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "DeepSeek完成约510亿元首轮外部融资：主要用于自研AI芯片和算力中心",
        "summary": "DeepSeek于2026年6月完成成立以来的首轮外部融资，筹集约510亿元人民币（约74亿美元），投后估值520至590亿美元。资金用途明确：扩建以国产芯片为主的算力中心、自研AI芯片、扩充全球顶尖人才团队。DeepSeek此前已在华为昇腾上完成V4模型训练，全面转向国产算力。",
        "source": "腾讯新闻",
        "url": "https://news.qq.com/rain/a/20260721A030HS00",
        "keywords": ["DeepSeek", "AI芯片", "国产算力", "昇腾", "融资"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "国内首个2万亿参数大模型跑通国产超节点，正式进入规模化商用阶段",
        "summary": "阿里真武M890×磐久AI128超节点成功适配Qwen3.8，并上线阿里云百炼平台提供模型推理服务，这是国内首个2万亿参数大模型在国产超节点上运行的案例，标志着国产超节点技术正式进入规模化商用阶段，多家厂商超节点产品正陆续落地AI核心业务场景。",
        "source": "网易订阅",
        "url": "https://www.163.com/dy/article/L2HQ2EPU0514D3UH.html",
        "keywords": ["Qwen3.8", "国产超节点", "阿里云", "端侧推理", "大模型"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "2026\"端侧AI战事\"升级：模型软硬协同成核心竞争力",
        "summary": "36氪分析指出，2026上半年端侧大模型进入新阶段，模型将继续变小变轻，但光靠压缩已不够，关键在于让模型与底层框架、芯片和具体设备场景配合，从\"能跑起来\"走向\"更好用\"。面壁智能已逐步将训练工作转移到国产芯片和国产集群，联合清华开源BitCPM-CANN，在华为昇腾平台验证1.58-bit三值大模型训练方案。",
        "source": "36氪",
        "url": "https://36kr.com/p/3864280705520640",
        "keywords": ["端侧AI", "面壁智能", "昇腾", "软硬协同", "大模型"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "tech",
        "categoryLabel": "技术前沿",
        "title": "多家人形机器人同台竞技，具身智能路线分化：生产力和家庭两条路径",
        "summary": "WAIC 2026观察：具身智能企业路线已明显分化，一条路径指向工厂产线、物流仓储、商业服务；另一条则指向家庭场景——情感陪伴、多代际沟通、日常生活。行业已从\"要不要做机器人\"走到\"做什么样的机器人\"的阶段，傅利叶等企业同期发布康养机器人居家场景方案。",
        "source": "新浪财经",
        "url": "https://finance.sina.com.cn/jjxw/2026-07-19/doc-iniiiwie8207206.shtml",
        "keywords": ["具身智能", "人形机器人", "家庭场景", "路线分化", "WAIC"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "京东发布AI Home实景样板间：JoyInside技术实现全屋主动式智能协同",
        "summary": "京东在WAIC 2026期间首次系统展示面向物理世界的JoyAI模型矩阵，并发布JoyAI-Talker语音模型，已形成覆盖语音、图像、视频、实时交互、世界模拟和具身智能的基础模型体系。AI Home实景样板间展示全屋主动式智能协同方案，JoyInside成为核心技术品牌。",
        "source": "中关村在线",
        "url": "https://ai.zol.com.cn/1217/12172622.html",
        "keywords": ["京东", "AI Home", "JoyInside", "全屋智能", "WAIC"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "product",
        "categoryLabel": "产品方案",
        "title": "2026全屋定制新趋势：AI智能体让家主动服务，装修阶段即同步设计",
        "summary": "2026年7月全屋定制装修与智能家居已从单品控制进化为以AI智能体为核心的\"零操作自主居家\"生态，业主在规划阶段需同步完成水电预埋、网络覆盖与七大核心系统的一体化设计，小米、海尔、华为等密集布局全屋智能赛道，AI智能体让家从\"听指令\"升级为\"主动服务\"。",
        "source": "新浪新闻",
        "url": "https://k.sina.com.cn/article_7880068385_1d5b04d2106801nhia.html?from=home",
        "keywords": ["全屋定制", "AI智能体", "智能家居", "主动服务", "装修设计"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "2026年消费者调研：80%智能家居用户要求设备厂商定期推送安全更新",
        "summary": "市场调研显示，截至2026年中，80%智能家居用户要求设备厂商定期提供安全更新，78%用户要求数据使用透明度，这一数据表明智能家居市场已走向成熟，用户隐私意识和安全需求显著提升，成为厂商差异化竞争的新战场。",
        "source": "Belinus",
        "url": "https://www.belinus.com/post/smart-home-advantages-what-homeowners-need-in-2026",
        "keywords": ["智能家居", "数据安全", "隐私保护", "安全更新", "用户需求"],
        "published": "2026-07-26"
    },
    {
        "date": "2026-07-26",
        "category": "security",
        "categoryLabel": "数据安全",
        "title": "全球IoT安全立法加速：美国加州物联网安全法与欧盟Cyber Resilience Act同步推进",
        "summary": "全球各国政府正加速出台物联网安全立法，美国加州物联网安全法和欧盟网络弹性法案（Cyber Resilience Act）同步推进，要求智能家居设备满足最低安全标准，包括禁止默认弱密码、要求安全更新、支持漏洞披露等，为智能家居行业设定了新的安全合规门槛。",
        "source": "MarTechDepot",
        "url": "https://www.martechdepot.com/2026/07/21/how-to-meet-the-iot-security-requirements-of-today-and-tomorrow/",
        "keywords": ["IoT安全", "物联网立法", "安全合规", "智能家居", "网络安全"],
        "published": "2026-07-26"
    }
]

# Filter out duplicates
added_news = []
skipped = 0
for n in new_news:
    if n['title'] not in existing_titles:
        existing_news.append(n)
        existing_titles.add(n['title'])
        added_news.append(n)
    else:
        skipped += 1

# Update lastUpdated
data['lastUpdated'] = '2026-07-26'

# Re-assign IDs
for i, n in enumerate(existing_news):
    n['id'] = i + 1

# Sort by date descending, then by id
def sort_key(n):
    try:
        from datetime import datetime
        d = datetime.strptime(n['date'], '%Y-%m-%d')
        return (-d.toordinal(), n['id'])
    except:
        return (0, n['id'])

existing_news.sort(key=sort_key)

# Re-assign IDs after sort
for i, n in enumerate(existing_news):
    n['id'] = i + 1

# Write back
with open('/Users/ma/.openclaw/workspace/smart-home-news-data/data.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Duplicates skipped: {skipped}')
print(f'New articles added: {len(added_news)}')
print(f'Total news count: {len(existing_news)}')
print(f'LastUpdated: {data["lastUpdated"]}')
print('Done!')
