"""
Keras example model factory functions.
"""

def get_model(name, **model_args):
    if name == 'cnn':
        from .cnn import build_model
        return build_model(**model_args)
    elif name == 'resnet_small':
        from .resnet import ResNetSmall
        return ResNetSmall(**model_args)
    elif name == 'resnet50':
        from .resnet import ResNet50
        return ResNet50(**model_args)
    elif name == 'rnn':
        from .rnn import build_model
        return build_model(**model_args)
    elif name == 'lstm_cnn':
        from .lstm_cnn import build_model
        return build_model(**model_args)
    elif name == 'lstm_cnn_merge':
        from .lstm_cnn_merge import build_model
        return build_model(**model_args)
    elif name == 'trend_plus_actuators':
        from .only_past_profiles_future_actuators import build_model
        return build_model(**model_args)
    elif name == 'joe_model':
        from .joe_architecture import build_model
        return build_model(**model_args)
    elif name == 'dif_lookbacks':
        from .dif_lookbacks import build_model
        return build_model(**model_args)
    else:
        raise ValueError('Model %s unknown' % name)
