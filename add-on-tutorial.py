import bpy

class HelloWorldPanel(bpy.types.Panel):
    bl_idname = "hello_wor"
    bl_label = "salutai"
    bl_space_type = 'SEQUENCE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "strawberry"

    def draw(self, context):
        self.layout.label(text="Hello World")
        self.layout.operator("mesh.primitive_cone_add", text = "Add Cone")

bpy.utils.register_class(HelloWorldPanel)

bl_info = {

    "name": "Hello World Add-On",
    "blender": (2,80,0),
    "category": "Object",
    
}

def register():
    bpy.utils.register_class(HelloWorldPanel)
def unregister():
     bpy.utils.unregister_class(HelloWorldPanel)
            