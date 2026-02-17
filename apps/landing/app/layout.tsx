import { libreBaskerville } from "@/lib/fonts"
import { metadata, viewport } from "@/lib/metadata"

import "@repo/ui/styles/globals.css"

export { metadata, viewport }

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${libreBaskerville.variable} font-serif antialiased`}>{children}</body>
    </html>
  )
}
