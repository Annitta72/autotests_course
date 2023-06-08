# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    """
    Вывод на печать, того что передано в маркер
    """
    # Здесь пишем код
    mark = request.node.get_closest_marker('id_check')
    print(*mark.args, sep='\n')
