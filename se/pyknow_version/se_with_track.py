from se.utils.decorators import time_track


@time_track
def run(ph=5.,
        vazao_produto=5.,
        vazao_agua_lavagem=130.,
        injecao_neutralizante=20.):

    from se.pyknow_version.engine import ESEngine
    from se.pyknow_version.engine import Data
    engine = ESEngine()
    engine.reset()
    engine.declare(Data(ph=ph,
                        vazao_produto=vazao_produto,
                        vazao_agua_lavagem=vazao_agua_lavagem,
                        injecao_neutralizante=injecao_neutralizante))
    engine.run()
