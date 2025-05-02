import unreal

def get_selected_assets():
    """Get selected assets from the Content Browser."""
    editor_utility = unreal.EditorUtilityLibrary()
    return editor_utility.get_selected_assets()

def spawn_actor_from_asset(asset, location, folder_name):
    """Spawn an actor in the level from the given asset and assign it to a folder."""
    if isinstance(asset, unreal.StaticMesh):
        # Spawn a StaticMeshActor
        actor = unreal.EditorLevelLibrary.spawn_actor_from_object(asset, location)
        if actor:
            actor.set_folder_path(folder_name)
            unreal.log(f"Spawned StaticMeshActor for asset: {asset.get_name()} at location: {location} in folder: {folder_name}")
        return actor
    elif isinstance(asset, unreal.BlueprintGeneratedClass):
        # Spawn an actor from a Blueprint class
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(asset, location)
        if actor:
            actor.set_folder_path(folder_name)
            unreal.log(f"Spawned Blueprint Actor for asset: {asset.get_name()} at location: {location} in folder: {folder_name}")
        return actor
    else:
        unreal.log_warning(f"Unsupported asset type: {asset.get_name()}")
        return None

def run():
    """Main function to create actors from selected assets."""
    selected_assets = get_selected_assets()

    if not selected_assets:
        unreal.log_error("No assets selected in the Content Browser.")
        return

    # Get the currently selected folder in the World Outliner
    folder_name = unreal.EditorUtilityLibrary.get_current_content_browser_path()

    unreal.log(f"Creating actors in folder: {folder_name}")

    # Starting position
    start_location = unreal.Vector(0, 0, 0)
    x_spacing = 150  # Distance between spawned actors along the X-axis
    z_spacing = 200  # Distance between rows along the Z-axis
    assets_per_row = 8  # Number of assets per row

    # Iterate through selected assets and spawn actors
    for index, asset in enumerate(selected_assets):
        row = index // assets_per_row
        col = index % assets_per_row
        location = unreal.Vector(
            start_location.x + col * x_spacing,
            start_location.y,
            start_location.z + row * z_spacing
        )
        spawn_actor_from_asset(asset, location, folder_name)

    unreal.log("Actor creation completed.")

# Run the script
run()