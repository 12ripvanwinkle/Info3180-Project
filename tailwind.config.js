/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      fontFamily: {
        pacifico: ['Pacifico', 'cursive'],
        ubuntu: ['Ubuntu', 'sans-serif'],
        spacegrotesk: ['Space Grotesk', 'sans-serif'],

      }
    },
  },
  plugins: [],
}

