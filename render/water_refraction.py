import math

def refract_uv(uv, normal, strength):
    """折射 UV。"""
    raise NotImplementedError("TODO: refract_uv")

def path_length(depth, view_z):
    """视线路径长度。"""
    raise NotImplementedError("TODO: path_length")

def absorption(distance, density):
    """水体吸收。"""
    raise NotImplementedError("TODO: absorption")

def caustic_facing(normal_z, threshold):
    """焦散朝向。"""
    raise NotImplementedError("TODO: caustic_facing")

def foam_mask(depth, object_id):
    """泡沫区域。"""
    raise NotImplementedError("TODO: foam_mask")

def reflect_camera_position(y, plane_y):
    """反射相机高度。"""
    raise NotImplementedError("TODO: reflect_camera_position")

def screen_edge_alpha(distance, fade):
    """屏幕边缘淡出。"""
    raise NotImplementedError("TODO: screen_edge_alpha")

def water_sort_key(layer, depth):
    """水面透明排序。"""
    raise NotImplementedError("TODO: water_sort_key")

def temporal_reset(wave_speed, threshold):
    """时域重置。"""
    raise NotImplementedError("TODO: temporal_reset")

def specular_once(base, reflection):
    """高光合成。"""
    raise NotImplementedError("TODO: specular_once")

def wave_normal_height(height, wavelength):
    """波浪法线。"""
    raise NotImplementedError("TODO: wave_normal_height")

def refraction_depth(current, previous):
    """折射深度选择。"""
    raise NotImplementedError("TODO: refraction_depth")

def caustic_scale(depth, base):
    """焦散尺度。"""
    raise NotImplementedError("TODO: caustic_scale")

def shoreline_alpha(depth, width):
    """岸线 alpha。"""
    raise NotImplementedError("TODO: shoreline_alpha")

def camera_matrix_key(camera_id):
    """相机矩阵键。"""
    raise NotImplementedError("TODO: camera_matrix_key")
