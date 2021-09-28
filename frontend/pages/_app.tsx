import '../styles/globals.css'
import { ChakraProvider } from '@chakra-ui/react'
import { AppProps } from 'next/app'

import Header from 'components/navigator/Header'

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Header/>
      <Component {...pageProps} />
    </ChakraProvider>
  )
}