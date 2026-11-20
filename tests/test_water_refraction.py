import pytest
from render import water_refraction as mod

CASES = [
    ("uv", 'm.refract_uv((0.5, 0.5), (0.2, -0.1), 0.5) == approx((0.6, 0.45))'),
    ("path", 'm.path_length(10, 2) == approx(5.0)'),
    ("absorption", 'm.absorption(10, 0.1) == approx(0.367879, rel=1e-5)'),
    ("facing", 'm.caustic_facing(0.8, 0.5) is True'),
    ("foam", 'm.foam_mask(0.2, 1) is True'),
    ("mirror", 'm.reflect_camera_position(5, 3) == approx(1.0)'),
    ("edge", 'm.screen_edge_alpha(2, 4) == approx(0.5)'),
    ("sort", 'm.water_sort_key(2, 5) == (2, -5)'),
    ("reset", 'm.temporal_reset(2.0, 1.0) is True'),
    ("spec", 'm.specular_once(2.0, 0.5) == approx(2.5)'),
    ("wave", 'm.wave_normal_height(0.4, 2.0) == approx(0.2)'),
    ("depth", 'm.refraction_depth(0, 9) == 9'),
    ("caustic", 'm.caustic_scale(5, 10) == approx(2.0)'),
    ("shore", 'm.shoreline_alpha(2, 4) == approx(0.5)'),
    ("key", 'm.camera_matrix_key("L") == "L"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
