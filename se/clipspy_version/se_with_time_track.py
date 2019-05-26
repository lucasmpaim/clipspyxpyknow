from se.utils.decorators import time_track


@time_track
def run(ph=5.,
        vazao_produto=5.,
        vazao_agua_lavagem=130.,
        injecao_neutralizante=20.):

    import clips
    env = clips.Environment()
    env.load('/app/se/clipspy_version/knowledge_base/base.clp')
    env.reset()
    env.assert_string(f'(data (ph {ph}) (vazao_produto {vazao_produto}) (vazao_agua_lavagem {vazao_agua_lavagem})'
                      f' (injecao_neutralizante {injecao_neutralizante}))')
    env.run()


if __name__ == '__main__':
    run()
