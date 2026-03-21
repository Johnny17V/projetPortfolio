/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "./templates/**/*.html",  // Si vos templates sont à la racine
      "./**/templates/**/*.html", // Pour les templates à l'intérieur de vos apps (ex: api/templates)
      "./static/**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

