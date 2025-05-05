export function photoUrl(filename) {
    return filename
      ? `/uploads/${filename}`
      : '/assets/default_picture.jpg';  
  }