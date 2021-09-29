import { NextPage } from 'next'

import { Box, Button, chakra, Spinner } from '@chakra-ui/react'
import LoadingMessage from 'components/navigator/LoadingMessage'

const Home: NextPage = () => {

  return (
    <div>
      <h1>Hello World!</h1>
      <Box>
        <chakra.h1 color="tomato">Hello World!</chakra.h1>
      </Box>
      <LoadingMessage></LoadingMessage>
      <Button colorScheme="blue">Button</Button>
    </div>
  )
}

export default Home