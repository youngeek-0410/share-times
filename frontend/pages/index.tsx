import {NextPage} from 'next'
import { Box, Button, chakra } from '@chakra-ui/react'

const Home: NextPage = () => {
  return(
    <div>
      <h1>Hello World!</h1>
      <Box>
        <chakra.h1 color="tomato">Hello World!</chakra.h1>
      </Box>
      <Button colorScheme="blue">Button</Button>
    </div>
  )
}

export default Home