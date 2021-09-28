import {NextPage} from 'next'

import { Wrap, WrapItem } from '@chakra-ui/layout'

import Card from 'components/pages/list/Card'

const List: NextPage = () => {
  return(
    <Wrap padding="10" spacing="30px" justify="center">
        {
            Array(25).fill(0).map(_ => 
                <WrapItem>
                    <Card />
                </WrapItem>
            )
        }
    </Wrap>
  )
}

export default List