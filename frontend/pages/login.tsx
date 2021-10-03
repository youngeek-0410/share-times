import { NextPage } from 'next'

import { Container, Box, Select, Input, Button, Text } from '@chakra-ui/react'

const Login: NextPage = () => {
    return (
        <Container centerContent padding="4">
            <Text fontSize="25px">ログイン</Text>
            <Box padding="2">
                <Box paddingBottom="4">
                    <label htmlFor="organization"><Text fontSize="large">展示名</Text></label>
                    <Select id="organization" placeholder="選択する">
                        <option value="option1">2-I</option>
                        <option value="option2">4-I</option>
                        <option value="option3">茶道部</option>
                    </Select>
                </Box>
                <Box paddingBottom="4">
                    <label htmlFor="password"><Text fontSize="large">パスワード</Text></label>
                    <Input id="password" placeholder="パスワードを入力" />
                </Box>
            </Box>
            <Button colorScheme="teal">ログイン</Button>
        </Container>
    )
}

export default Login