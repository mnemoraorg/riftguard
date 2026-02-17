import type { Metadata } from "next"
import { libreBaskerville, inter } from "@/lib/fonts"
import { metadata } from "@/lib/metadata"
import "@repo/ui/styles/globals.css"

export { metadata }

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${libreBaskerville.variable} ${inter.variable} antialiased`}>
        {children}
      </body>
    </html>
  )
}
