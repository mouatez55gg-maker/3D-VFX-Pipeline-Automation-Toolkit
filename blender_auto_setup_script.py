import bpy

def setup_scene():
    """
    Automates basic scene setup in Blender:
    - Clears default objects
    - Sets render engine to Cycles
    - Creates a 3-point lighting setup
    - Adds a camera
    """
    # 1. Clear existing mesh objects to start fresh
    bpy.ops.object.select_all(action='DESELECT')
    for obj in bpy.context.scene.objects:
        if obj.type in {'MESH', 'LIGHT', 'CAMERA'}:
            obj.select_set(True)
    bpy.ops.object.delete()

    # 2. Set Render Engine to Cycles for high-quality rendering
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'
    
    # 3. Create 3-Point Lighting
    light_data = [
        {"name": "Key_Light", "location": (5, -5, 5), "energy": 1000},
        {"name": "Fill_Light", "location": (-5, -5, 3), "energy": 500},
        {"name": "Rim_Light", "location": (0, 5, 5), "energy": 1500}
    ]
    
    for ld in light_data:
        light_data_block = bpy.data.lights.new(name=ld["name"], type='AREA')
        light_data_block.energy = ld["energy"]
        light_obj = bpy.data.objects.new(name=ld["name"], object_data=light_data_block)
        bpy.context.collection.objects.link(light_obj)
        light_obj.location = ld["location"]

    # 4. Add Main Camera
    cam_data = bpy.data.cameras.new("Main_Camera")
    cam_obj = bpy.data.objects.new("Main_Camera", cam_data)
    bpy.context.collection.objects.link(cam_obj)
    cam_obj.location = (0, -10, 5)
    cam_obj.rotation_euler = (1.1, 0, 0) # Angled slightly down
    bpy.context.scene.camera = cam_obj

    print("Pipeline Automation: Scene setup complete.")

if __name__ == "__main__":
    setup_scene()