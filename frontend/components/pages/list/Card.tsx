import { FC } from 'react'
import { Box, Flex, Spacer, Text } from '@chakra-ui/react'

const Card: FC = () => {
    return(
        <Box maxW="300" borderWidth="1px" borderRadius="lg" overflow="hidden">
            <Box d="flex" alignItems="baseline" bgColor="teal.100" padding={3} paddingBottom="1.5">
                <Spacer/>
                <Text fontWeight='bold' fontSize="60">19</Text>
                <Text marginLeft="2">分</Text>
                <Spacer/>
            </Box>
            <Flex padding="3" borderTop="1px" borderTopColor="gray.100">
                <Text fontSize="20" marginLeft="1" letterSpacing="wider">コンピュータ部</Text>
                <Spacer minWidth="2" />
                <Text margin="auto" color="gray.600" fontSize="12px">5分前に更新</Text>
            </Flex>
        </Box>
    )
}

export default Card