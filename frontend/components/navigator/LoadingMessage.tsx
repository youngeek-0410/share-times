import { FC } from 'react'
import { HStack, Spinner, Text } from '@chakra-ui/react'

const LoadingMessage: FC = () => {
    return (
        <HStack alignContent="baseline">
            <Spinner
                thickness="4px"
                speed="0.7s"
                emptyColor="gray.200"
                color="teal"
                size="lg"
            />
            <Text padding="2" margin="auto">
                読み込み中...
            </Text>
        </HStack>
    )
}

export default LoadingMessage