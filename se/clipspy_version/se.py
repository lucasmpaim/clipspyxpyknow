from se.utils.helpers import pyread_float


def run(with_fix='n'):
    import clips

    file_name = 'base.clp' if with_fix == 'n' else 'base_with_fix_reader.clp'

    env = clips.Environment()
    env.define_function(pyread_float)
    env.load(f'/app/se/clipspy_version/knowledge_base/{file_name}')
    env.reset()

    env.run()


if __name__ == '__main__':
    run()
