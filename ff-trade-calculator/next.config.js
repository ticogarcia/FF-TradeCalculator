/** @type {import('next').NextConfig} */
const nextConfig = {}

module.exports = nextConfig

// module.exports = {
//     webpack: (config, { isServer }) => {
//       // Fixes npm packages that depend on `fs` module
//       if (!isServer) {
//         config.node = {
//           fs: 'empty'
//         }
//       }
  
//       return config
//     }
//   }
