import { defineConfig } from 'vite'
import { resolve } from 'path'

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        story: resolve(__dirname, 'our-story.html'),
        experience: resolve(__dirname, 'the-experience.html'),
        menu: resolve(__dirname, 'interactive-menu.html'),
        contact: resolve(__dirname, 'contact-reservations.html')
      }
    }
  }
})
