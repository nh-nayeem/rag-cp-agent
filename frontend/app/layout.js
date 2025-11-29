import './globals.css'

export const metadata = {
  title: 'RAG CP Agent',
  description: 'A RAG-based agent for competitive programming',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}