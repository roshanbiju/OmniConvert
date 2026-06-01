def export_image(
    model,
    output_path
):

    img = model.image

    if output_path.endswith(".jpg"):
        img = img.convert("RGB")

    img.save(output_path)