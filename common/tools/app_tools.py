from common.models import Sequence


def next_val(scope: str, zfill: int = 9):
    """ Function for next sequence value """
    try:
        seq = Sequence.objects.get(scope=scope)
        seq.crt_value = seq.crt_value + 1
        seq.save()
    except Sequence.DoesNotExist:
        seq = Sequence(scope=scope, crt_value=0)
        seq.save()
    return str(seq.crt_value).zfill(zfill)
