import bpy
    
       
class CAMERA_PT_change_view(bpy.types.Panel):
    bl_idname = "camera_cycler"
    bl_label = "Camera Cycler"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Camera Cycler"

    
    
           
            
    
    def draw (self, context):
      
     
   
        self.layout.label(text = "Add Camera")
        self.layout.operator("object.camera_add", text = "Add Camera")
        self.layout.label(text = "Change Camera View")
        self.layout.operator("camera.change_view", text = "Change View")
        
class CAMERA_OT_change_view (bpy.types.Operator):
     
    
        bl_idname = "camera.change_view"
        bl_label = "Change the camera in which you are viewing the objects through"
        
        def execute (self, context):
            cameras = [obj for obj in context.scene.objects if obj.type == 'CAMERA']
            scene = context.scene
            if scene.camera in cameras:
                index = cameras.index(scene.camera)
                index = (index + 1) % len(cameras)
            else:
                index = 0
            scene.camera = cameras[index]

       
            bpy.ops.view3d.view_camera()
            return {"FINISHED"}
        
        bl_info  = {
            "name": "Camera Cycler Add-On",
            "blender" : {2, 80, 0} ,
            "category" : "Object" , 
        }

def register ():
    bpy.utils.register_class(CAMERA_PT_change_view)
    bpy.utils.register_class(CAMERA_OT_change_view)
     
def unregister ():
    bpy.utils.unregister_class(CAMERA_PT_change_view)
    bpy.utils.unregister_class(CAMERA_OT_change_view)
    

if __name__ == "__main__":
    register()
    
        
     
           
        
