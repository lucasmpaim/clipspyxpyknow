from se.utils.decorators import time_track


@time_track
def run():
    import clips
    env = clips.Environment()
    env.load('/app/se/clipspy_version/knowledge_base/base.clp')
    env.reset()
    env.assert_string('(data (ph 5.0) (vazao_produto 5.0) (vazao_agua_lavagem 130.0) (injecao_neutralizante 20.0))')
    env.run()


if __name__ == '__main__':
    run()
