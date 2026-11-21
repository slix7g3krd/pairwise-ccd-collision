import pytest
import math
from gameplay import ccd_collision as mod

CASES = [
    ("swept", 'm.swept_hit(0, 2, 1) is True'),
    ("side", 'm.side_hit((1, 0, 0), (0, 0, 0, 1, 1, 1)) is True'),
    ("rotation", 'm.rotation_cover(90, 2) == 180'),
    ("bounce", 'm.bounce_time(0.1, 2) == approx(0.05)'),
    ("trigger", 'm.trigger_radius(1, 2) == 2'),
    ("platform", 'm.platform_sweep(5) == 5'),
    ("joint", 'm.joint_iterations(5) == 20'),
    ("sync", 'm.sync_event(3) == 3'),
    ("bilinear", 'm.bilinear(0, 0, 10, 10, 0.5) == approx(5.0)'),
    ("adaptive", 'm.adaptive_iterations(2, 4) == 8'),
    ("impact", 'm.impact_point(0, 10, 0.5) == approx(5.0)'),
    ("key", 'm.ccd_key(3, 2) == "3:2"'),
    ("tunnel", 'm.is_tunneling(2, 0.05) is True'),
    ("toi", 'm.time_of_impact(4, 2) == approx(2.0)'),
    ("valid", 'm.valid_toi(0.5) is True')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
