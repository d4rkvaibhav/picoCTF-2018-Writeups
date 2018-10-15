Problem Statement(150 points):

Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell2.picoctf.com 18581.

Solution :
 
 I was given the following ciphertext :

	-------------------------------------------------------------------------------
	wgzivhot ymvm ut jglv achi - tlqtouolougz_wusymvt_hvm_tgcbhqcm_yhaxzqgmtb
	-------------------------------------------------------------------------------
	tohomcj, sclfs qlwr flccuihz whfm avgf oym tohuvymhx, qmhvuzi h qgnc ga
	choymv gz nyuwy h fuvvgv hzx h vhpgv chj wvgttmx. h jmccgn xvmttuziignz,
	lziuvxcmx, nht tltohuzmx imzocj qmyuzx yuf gz oym fucx fgvzuzi huv. ym
	ymcx oym qgnc hcgao hzx uzogzmx:

	-uzovguqg hx hcohvm xmu.

	yhcomx, ym smmvmx xgnz oym xhvr nuzxuzi tohuvt hzx whccmx glo wghvtmcj:

	-wgfm ls, ruzwy! wgfm ls, jgl amhvalc emtluo!

	tgcmfzcj ym whfm agvnhvx hzx fglzomx oym vglzx ilzvmto. ym ahwmx hqglo
	hzx qcmttmx ivhbmcj oyvuwm oym ognmv, oym tlvvglzxuzi chzx hzx oym
	hnhruzi fglzohuzt. oymz, whowyuzi tuiyo ga tomsymz xmxhclt, ym qmzo
	ognhvxt yuf hzx fhxm vhsux wvgttmt uz oym huv, ilvicuzi uz yut oyvgho
	hzx tyhruzi yut ymhx. tomsymz xmxhclt, xutscmhtmx hzx tcmmsj, cmhzmx
	yut hvft gz oym ogs ga oym tohuvwhtm hzx cggrmx wgcxcj ho oym tyhruzi
	ilvicuzi ahwm oyho qcmttmx yuf, mdluzm uz uot cmzioy, hzx ho oym cuiyo
	lzogztlvmx yhuv, ivhuzmx hzx ylmx curm shcm ghr.

	qlwr flccuihz smmsmx hz uztohzo lzxmv oym fuvvgv hzx oymz wgbmvmx oym
	qgnc tfhvocj.

	-qhwr og qhvvhwrt! ym thux tomvzcj.

	ym hxxmx uz h svmhwymvt ogzm:

	-agv oyut, g xmhvcj qmcgbmx, ut oym imzluzm wyvutouzm: qgxj hzx tglc
	hzx qcggx hzx glzt. tcgn fltuw, scmhtm. tylo jglv mjmt, imzot. gzm
	fgfmzo. h cuoocm ovglqcm hqglo oygtm nyuom wgvsltwcmt. tucmzwm, hcc.

	ym smmvmx tuxmnhjt ls hzx ihbm h cgzi tcgn nyutocm ga whcc, oymz shltmx
	hnyucm uz vhso hoomzougz, yut mbmz nyuom ommoy icutomzuzi ymvm hzx oymvm
	nuoy igcx sguzot. wyvjtgtogfgt. ong tovgzi tyvucc nyutocmt hztnmvmx
	oyvgliy oym whcf.

	-oyhzrt, gcx wyhs, ym wvumx qvutrcj. oyho nucc xg zuwmcj. tnuowy gaa
	oym wlvvmzo, nucc jgl?

	ym trussmx gaa oym ilzvmto hzx cggrmx ivhbmcj ho yut nhowymv, ihoymvuzi
	hqglo yut cmit oym cggtm agcxt ga yut ignz. oym sclfs tyhxgnmx ahwm hzx
	tlccmz gbhc egnc vmwhccmx h svmchom, shovgz ga hvot uz oym fuxxcm himt.
	h scmhthzo tfucm qvgrm dlumocj gbmv yut cust.

As the question name tells hertz which means frequency.So we have to do frequency analysis.I decoded it with 

http://crypto.interactive-maths.com/frequency-analysis-breaking-the-code.html and make following substitution

	M H O Z T G C U Y X V L I W S N F Q J A R B D E P K 
	| | | | | | | | | | | | | | | | | | | | | | | | | | 
	e a t n s o l i h d r u g c p w m b y f k v     z

Using the above substitution gave me the flag :

congrats here is your flag - substitution_ciphers_are_solvable_hafdnboesv


	picoCTF{substitution_ciphers_are_solvable_hafdnboesv}