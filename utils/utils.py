import os

def photo_upload_to(instance, filename):
    school_name = instance.name.replace(' ', '_')
    return os.path.join('photos', school_name, filename)
