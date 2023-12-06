import model
import service
import config


if __name__ == "__main__":
    connectApiCC= model.ApiCC(
                                "40B8D99A-FBA8-4755-BF27-0C454F3F27C8",
                                "399e840d28361946",
                                "2969d025-df54-4b96-ae54-2b2100e053b0",
                                "1310"
                                )
    connectBancoCC = model.ConectarBanco(1310, config.ssl_config)
    dfDocumentos = connectApiCC.requestDocumentos()
    dfPadrapoNomenclatura = connectBancoCC.listarPadrao()
    objetoTeste = service.SincComPadrao(dfDocumentos, dfPadrapoNomenclatura)
    print(objetoTeste.testeDisciplinas())
    
    