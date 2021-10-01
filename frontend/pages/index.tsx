import {NextPage} from 'next'

import { Box, Button, chakra, Spinner } from '@chakra-ui/react'
import ListControlBar from 'components/pages/list/ListControlBar'

const Home: NextPage = () => {
  return(
    <div>
      <h1>Hello World!</h1>
      <Box>
        <chakra.h1 color="tomato">Hello World!</chakra.h1>
      </Box>
      <Button colorScheme="blue">Button</Button>
      <ListControlBar />
    </div>
  )
}

export default Home