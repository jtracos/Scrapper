#smn
#imgFc24h = "//div[@class=\"col-lg-6 col-md-6\"]/div/a/img/@src"
#smn = "https://smn.conagua.gob.mx/es/pronosticos/pronosticossubmenu/pronostico-meteorologico-especial-cuencas-96h"
#TH

#TH = 'https://www.tabascohoy.com'

#LINKS = '//div/div/a[@rel=\"bookmark\"]/div/div/h2/../../.././@href'
#TITLE = '//div/div/a[@rel="bookmark"]/div/div/h2/text()'


DP = "https://www.diariopresente.mx"
#vinculo de la pagina principal
DP_LINKS = "//article/div[@class = 'detail']/div[@class='info']/span/i[@class='fa fa-calendar-o']/../../..//div[contains(@class,'caption')]/a/@href"
#fechas en el home
DP_DATE = "//article/div[@class = 'detail']/div/span/i[@class='fa fa-calendar-o']/../text()"
#encabezos de la notas en el home
DP_HEADER = "//article/div[@class = 'detail']/div[@class='info']/span/i[@class='fa fa-calendar-o']/../../..//div[contains(@class,'caption')]/a/text()"
#titulo de la nota
AR_TITLE = "//div/div[@class='caption']/text()"
#resumen de la nota
AR_RESUMEE = "//div[@class='detail']/div[contains(@style,'color')]/text()"
#cuerpo de la nota
AR_BODY = "//p/span/font/text()"
#fecha de la nota
AR_DATE = "//div[@class='detail']/div[@class='info']/span[@class='date']/i[@class='fa fa-calendar-o']/../text()"