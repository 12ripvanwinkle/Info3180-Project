export function photoUrl(filename) {
    return filename
      ? `/uploads/${filename}`
      : '/uploads/default_picture.jpg';  
  }