import unreal

def layout_selected_actors(x_spacing=300, z_spacing=300):
    """Layout selected actors in the level with specified spacing and reset their rotation."""
    selected_actors = unreal.EditorLevelLibrary.get_selected_level_actors()

    if not selected_actors:
        unreal.log_error("No actors selected in the level.")
        return

    start_location = unreal.Vector(0, 0, 0)
    assets_per_row = 6  # Number of actors per row

    for index, actor in enumerate(selected_actors):
        row = index // assets_per_row
        col = index % assets_per_row
        new_location = unreal.Vector(
            start_location.x + col * x_spacing,
            start_location.y,
            start_location.z + row * z_spacing
        )
        actor.set_actor_location(new_location, False, True)
        
        # Reset actor rotation to (0, 0, 0)
        new_rotation = unreal.Rotator(0, 0, 0)
        actor.set_actor_rotation(new_rotation, False)

    unreal.log("Actors have been laid out and their rotation reset successfully.")

# Run the layout function
layout_selected_actors()