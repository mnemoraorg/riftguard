import type { Metadata, Viewport } from "next";

const appName = "Riftguard";
const appDescription =
  "Riftguard predicts tsunamis by analyzing earthquake signals in real time. It spots dangerous patterns early, giving life-saving warnings before waves hit coastal areas.";

export const metadata: Metadata = {
  metadataBase: new URL("https://riftguard.mnemora.org"),
  applicationName: appName,
  title: {
    default: appName,
    template: `%s | ${appName}`,
  },
  description: appDescription,
  keywords: ["tsunami prediction", "earthquake analysis", "real-time alerts", "disaster warning", "safety"],
  authors: [{ name: "Mnemora Team" }],
  creator: "Mnemora",
  openGraph: {
    type: "website",
    title: appName,
    description: appDescription,
    siteName: appName,
    url: "https://riftguard.mnemora.org",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: `${appName} - Tsunami Prediction System`,
      },
    ],
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: appName,
    description: appDescription,
    creator: "@mnemora",
    images: ["/og-image.png"],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
  width: "device-width",
  initialScale: 1,
  maximumScale: 1,
};
