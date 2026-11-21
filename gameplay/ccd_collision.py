import math

def swept_hit(start, end, plane):
    """扫掠命中。"""
    raise NotImplementedError("TODO: swept_hit")

def side_hit(point, box):
    """侧面扫掠。"""
    raise NotImplementedError("TODO: side_hit")

def rotation_cover(angle, radius):
    """旋转体积。"""
    raise NotImplementedError("TODO: rotation_cover")

def bounce_time(penetration, speed):
    """反弹时间。"""
    raise NotImplementedError("TODO: bounce_time")

def trigger_radius(radius, extent):
    """触发器体积。"""
    raise NotImplementedError("TODO: trigger_radius")

def platform_sweep(delta):
    """平台扫掠。"""
    raise NotImplementedError("TODO: platform_sweep")

def joint_iterations(distance):
    """关节迭代。"""
    raise NotImplementedError("TODO: joint_iterations")

def sync_event(hit):
    """同步碰撞事件。"""
    raise NotImplementedError("TODO: sync_event")

def bilinear(a, b, c, d, t):
    """双线性采样。"""
    raise NotImplementedError("TODO: bilinear")

def adaptive_iterations(distance, base):
    """自适应迭代。"""
    raise NotImplementedError("TODO: adaptive_iterations")

def impact_point(start, end, t):
    """撞击点。"""
    raise NotImplementedError("TODO: impact_point")

def ccd_key(seed, index):
    """CCD 键。"""
    raise NotImplementedError("TODO: ccd_key")

def is_tunneling(delta, thickness):
    """穿透判定。"""
    raise NotImplementedError("TODO: is_tunneling")

def time_of_impact(distance, speed):
    """TOI。"""
    raise NotImplementedError("TODO: time_of_impact")

def valid_toi(t):
    """TOI 合法。"""
    raise NotImplementedError("TODO: valid_toi")
