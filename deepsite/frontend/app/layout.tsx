import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: '5DSens DeepSite',
  description: 'Infrastructure Dashboard',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
