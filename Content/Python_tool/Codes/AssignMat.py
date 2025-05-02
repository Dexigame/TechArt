import unreal

def get_selected_assets():
    """Get selected assets from the Content Browser."""
    editor_utility = unreal.EditorUtilityLibrary()
    return editor_utility.get_selected_assets()

def get_selected_actors():
    """Get selected actors in the level."""
    editor_level_library = unreal.EditorLevelLibrary()
    return editor_level_library.get_selected_level_actors()

def assign_material_to_static_mesh(static_mesh, material, material_index=0):
    """Assign a material to a static mesh."""
    static_mesh_editor_subsystem = unreal.get_editor_subsystem(unreal.StaticMeshEditorSubsystem)
    static_mesh_editor_subsystem.set_material(static_mesh, material_index, material)

def assign_material_to_actor(actor, material, material_index=0):
    """Assign a material to an actor's static mesh component."""
    static_mesh_component = actor.get_component_by_class(unreal.StaticMeshComponent)
    if static_mesh_component:
        static_mesh_component.set_material(material_index, material)

def run():
    """Main function to assign material or material instance."""
    unreal.log("Assigning Material to Selected Objects...")

    # Get selected assets and actors
    selected_assets = get_selected_assets()
    selected_actors = get_selected_actors()

    # Find the first material or material instance in the selected assets
    material = next((asset for asset in selected_assets if isinstance(asset, (unreal.Material, unreal.MaterialInstance))), None)

    if not material:
        unreal.log_error("No material or material instance selected.")
        return

    unreal.log(f"Selected material: {material.get_name()}")

    # Assign material to selected static meshes in the Content Browser
    for asset in selected_assets:
        if isinstance(asset, unreal.StaticMesh):
            assign_material_to_static_mesh(asset, material)
            unreal.log(f"Assigned material {material.get_name()} to static mesh {asset.get_name()}")

    # Assign material to selected actors in the level
    for actor in selected_actors:
        assign_material_to_actor(actor, material)
        unreal.log(f"Assigned material {material.get_name()} to actor {actor.get_name()}")

    unreal.log("Material assignment completed.")

# Run the script
run()