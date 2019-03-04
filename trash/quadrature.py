def quadrature_xi_wi(n):
    if not isinstance(n, int):
        raise RuntimeError('n must be an integer')
    if n < 2:
        raise RuntimeError('n must be at least 2')
    xi = [0]*n
    wi = [0]*n
    if n == 2:
        xi[0] = -0.577350269189625764509148780501957455647601751270126876
        xi[1] = 0.577350269189625764509148780501957455647601751270126876
        wi[0] = 1.
        wi[1] = 1.
    elif n == 3:
        xi[0] = -0.774596669241483377035853079956479922166584341058318165
        xi[1] = 0
        xi[2] = 0.774596669241483377035853079956479922166584341058318165
        wi[0] = 0.555555555555555555555555555555555555555555555555555556
        wi[1] = 0.888888888888888888888888888888888888888888888888888889
        wi[2] = 0.555555555555555555555555555555555555555555555555555556
    elif n == 4:
        xi[0] = -0.861136311594052575223946488892809505095725379629717638
        xi[1] = -0.339981043584856264802665759103244687200575869770914353
        xi[2] = 0.339981043584856264802665759103244687200575869770914353
        xi[3] = 0.861136311594052575223946488892809505095725379629717638
        wi[0] = 0.34785484513745385737306394922199940723534869583389354
        wi[1] = 0.65214515486254614262693605077800059276465130416610646
        wi[2] = 0.65214515486254614262693605077800059276465130416610646
        wi[3] = 0.34785484513745385737306394922199940723534869583389354
    elif n == 5:
        xi[0] = -0.906179845938663992797626878299392965125651910762530863
        xi[1] = -0.538469310105683091036314420700208804967286606905559956
        xi[2] = 0
        xi[3] = 0.538469310105683091036314420700208804967286606905559956
        xi[4] = 0.906179845938663992797626878299392965125651910762530863
        wi[0] = 0.236926885056189087514264040719917362643260002212414016
        wi[1] = 0.47862867049936646804129151483563819291229555334314154
        wi[2] = 0.568888888888888888888888888888888888888888888888888889
        wi[3] = 0.47862867049936646804129151483563819291229555334314154
        wi[4] = 0.236926885056189087514264040719917362643260002212414016
    elif n == 6:
        xi[0] = -0.932469514203152027812301554493994609134765737712289825
        xi[1] = -0.661209386466264513661399595019905347006448564395170071
        xi[2] = -0.23861918608319690863050172168071193541861063014002135
        xi[3] = 0.23861918608319690863050172168071193541861063014002135
        xi[4] = 0.661209386466264513661399595019905347006448564395170071
        xi[5] = 0.932469514203152027812301554493994609134765737712289825
        wi[0] = 0.171324492379170345040296142172732893526822501484043982
        wi[1] = 0.360761573048138607569833513837716111661521892746745482
        wi[2] = 0.467913934572691047389870343989550994811655605769210535
        wi[3] = 0.467913934572691047389870343989550994811655605769210535
        wi[4] = 0.360761573048138607569833513837716111661521892746745482
        wi[5] = 0.171324492379170345040296142172732893526822501484043982
    elif n == 7:
        xi[0] = -0.949107912342758524526189684047851262400770937670617784
        xi[1] = -0.74153118559939443986386477328078840707414764714139026
        xi[2] = -0.405845151377397166906606412076961463347382014099370126
        xi[3] = 0
        xi[4] = 0.405845151377397166906606412076961463347382014099370126
        xi[5] = 0.74153118559939443986386477328078840707414764714139026
        xi[6] = 0.949107912342758524526189684047851262400770937670617784
        wi[0] = 0.129484966168869693270611432679082018328587402259946664
        wi[1] = 0.279705391489276667901467771423779582486925065226598765
        wi[2] = 0.381830050505118944950369775488975133878365083533862735
        wi[3] = 0.417959183673469387755102040816326530612244897959183673
        wi[4] = 0.381830050505118944950369775488975133878365083533862735
        wi[5] = 0.279705391489276667901467771423779582486925065226598765
        wi[6] = 0.129484966168869693270611432679082018328587402259946664
    elif n == 8:
        xi[0] = -0.960289856497536231683560868569472990428235234301452038
        xi[1] = -0.796666477413626739591553936475830436837171731615964832
        xi[2] = -0.525532409916328985817739049189246349041964243120392858
        xi[3] = -0.183434642495649804939476142360183980666757812912973782
        xi[4] = 0.183434642495649804939476142360183980666757812912973782
        xi[5] = 0.525532409916328985817739049189246349041964243120392858
        xi[6] = 0.796666477413626739591553936475830436837171731615964832
        xi[7] = 0.960289856497536231683560868569472990428235234301452038
        wi[0] = 0.1012285362903762591525313543099621901153940910516849571
        wi[1] = 0.222381034453374470544355994426240884430130870051249565
        wi[2] = 0.313706645877887287337962201986601313260328999002734938
        wi[3] = 0.362683783378361982965150449277195612194146039894330541
        wi[4] = 0.362683783378361982965150449277195612194146039894330541
        wi[5] = 0.313706645877887287337962201986601313260328999002734938
        wi[6] = 0.222381034453374470544355994426240884430130870051249565
        wi[7] = 0.1012285362903762591525313543099621901153940910516849571
    elif n == 9:
        xi[0] = -0.96816023950762608983557620290367287004940480049192533
        xi[1] = -0.836031107326635794299429788069734876544106718124675996
        xi[2] = -0.613371432700590397308702039341474184785720604940564693
        xi[3] = -0.324253423403808929038538014643336608571956260736973089
        xi[4] = 0
        xi[5] = 0.324253423403808929038538014643336608571956260736973089
        xi[6] = 0.613371432700590397308702039341474184785720604940564693
        xi[7] = 0.836031107326635794299429788069734876544106718124675996
        xi[8] = 0.96816023950762608983557620290367287004940480049192533
        wi[0] = 0.0812743883615744119718921581105236506756617207824107507
        wi[1] = 0.180648160694857404058472031242912809514337821732040484
        wi[2] = 0.260610696402935462318742869418632849771840204437299952
        wi[3] = 0.312347077040002840068630406584443665598754861261904646
        wi[4] = 0.330239355001259763164525069286974048878810783572688335
        wi[5] = 0.312347077040002840068630406584443665598754861261904646
        wi[6] = 0.260610696402935462318742869418632849771840204437299952
        wi[7] = 0.180648160694857404058472031242912809514337821732040484
        wi[8] = 0.0812743883615744119718921581105236506756617207824107507
    elif n == 10:
        xi[0] = -0.973906528517171720077964012084452053428269946692382119
        xi[1] = -0.865063366688984510732096688423493048527543014965330453
        xi[2] = -0.679409568299024406234327365114873575769294711834809468
        xi[3] = -0.433395394129247190799265943165784162200071837656246497
        xi[4] = -0.148874338981631210884826001129719984617564859420691696
        xi[5] = 0.148874338981631210884826001129719984617564859420691696
        xi[6] = 0.433395394129247190799265943165784162200071837656246497
        xi[7] = 0.679409568299024406234327365114873575769294711834809468
        xi[8] = 0.865063366688984510732096688423493048527543014965330453
        xi[9] = 0.973906528517171720077964012084452053428269946692382119
        wi[0] = 0.0666713443086881375935688098933317928578648343201581451
        wi[1] = 0.149451349150580593145776339657697332402556639669427368
        wi[2] = 0.21908636251598204399553493422816319245877187052267709
        wi[3] = 0.269266719309996355091226921569469352859759938460883796
        wi[4] = 0.295524224714752870173892994651338329421046717026853601
        wi[5] = 0.295524224714752870173892994651338329421046717026853601
        wi[6] = 0.269266719309996355091226921569469352859759938460883796
        wi[7] = 0.21908636251598204399553493422816319245877187052267709
        wi[8] = 0.149451349150580593145776339657697332402556639669427368
        wi[9] = 0.0666713443086881375935688098933317928578648343201581451
    else:
        raise NotImplementedError('n > 10 not implemented')
    return xi, wi