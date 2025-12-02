def wrap_map(fn, needs_args=False):
    def call(player, box, button, end):
        if needs_args:
            result = fn(player, box, button, end)
        else:
            result = fn()
        
        # Normalize return values
        if len(result) == 2:  # no doors
            walls, imgs = result
            doors = None
        else:
            walls, doors, imgs = result
        
        return walls, doors, imgs
    return call
